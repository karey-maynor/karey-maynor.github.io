#!/usr/bin/env python3
"""
Add new publications from an ORCID record to _bibliography/papers.bib.

How it works
  1. Reads the public works list for ORCID_ID from the ORCID public API.
  2. Skips anything already in papers.bib (matched by DOI, then by title),
     anything listed in _bibliography/orcid_ignore.txt, and works without a DOI.
  3. Downloads a BibTeX record for each new DOI from doi.org (Crossref as a fallback).
  4. Tidies it for al-folio (readable key, journal `abbr`, `altmetric`,
     `bibtex_show`, `html` link) and appends it to papers.bib.

It only ever ADDS entries. Existing entries, and any edits you made to them,
are never changed.

Usage
  python3 bin/update_bib_from_orcid.py            # update papers.bib
  python3 bin/update_bib_from_orcid.py --dry-run  # show what would be added, change nothing

Uses only the Python standard library.
"""

import argparse
import html
import json
import os
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request

# --------------------------------------------------------------------------- #
# Settings (can be overridden with environment variables in the workflow)
# --------------------------------------------------------------------------- #
ORCID_ID = os.environ.get("ORCID_ID", "0009-0009-3351-8408")
BIB_FILE = os.environ.get("BIB_FILE", "_bibliography/papers.bib")
IGNORE_FILE = os.environ.get("IGNORE_FILE", "_bibliography/orcid_ignore.txt")

# ORCID work types to import. Others (datasets, posters, etc.) are skipped.
INCLUDE_TYPES = set(
    t.strip()
    for t in os.environ.get(
        "INCLUDE_TYPES", "journal-article,conference-paper,book,book-chapter,review"
    ).split(",")
    if t.strip()
)

# Journal name -> the abbreviation shown in the badge on your publications page.
# Matching ignores case. Anything not listed gets initials, e.g.
# "International Journal of Greenhouse Gas Control" -> "IJGGC".
JOURNAL_ABBR = {
    "international journal of greenhouse gas control": "IJGGC",
    # "environmental science & technology": "ES&T",
}

USER_AGENT = "al-folio-orcid-sync/1.0 (+https://github.com/alshedivat/al-folio)"
CROSSREF_MAILTO = os.environ.get("CROSSREF_MAILTO", "")  # optional, for Crossref's polite pool

# --------------------------------------------------------------------------- #
# Small helpers
# --------------------------------------------------------------------------- #


def http_get(url, accept, retries=3):
    headers = {"Accept": accept, "User-Agent": USER_AGENT}
    last_err = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=30) as resp:
                return resp.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            last_err = e
            if e.code in (404, 406):  # not found / format unavailable: no point retrying
                break
        except Exception as e:  # network hiccup
            last_err = e
        time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"GET {url} failed: {last_err}")


def normalize_doi(doi):
    doi = (doi or "").strip().lower()
    doi = re.sub(r"^(https?://)?(dx\.)?doi\.org/", "", doi)
    doi = re.sub(r"^doi:\s*", "", doi)
    return doi.strip()


def normalize_title(title):
    title = re.sub(r"[{}\\]", "", title or "")
    title = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]", "", title.lower())


def ascii_slug(text):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]", "", text.lower())


# --------------------------------------------------------------------------- #
# Minimal BibTeX parsing (enough for Crossref output and for reading papers.bib)
# --------------------------------------------------------------------------- #


def split_entries(text):
    """Yield the raw text of each @type{...} entry in a .bib file."""
    i = 0
    while True:
        at = text.find("@", i)
        if at == -1:
            return
        brace = text.find("{", at)
        if brace == -1:
            return
        etype = text[at + 1 : brace].strip().lower()
        depth, j = 0, brace
        while j < len(text):
            if text[j] == "{":
                depth += 1
            elif text[j] == "}":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        if etype not in ("comment", "string", "preamble"):
            yield text[at : j + 1]
        i = j + 1


def parse_entry(raw):
    """Return (type, key, [(field, value_as_written)]) for one entry."""
    m = re.match(r"@\s*(\w+)\s*\{\s*([^,\s]*)\s*,", raw, re.S)
    if not m:
        return None
    etype, key = m.group(1).lower(), m.group(2)
    body = raw[m.end() : raw.rfind("}")]
    fields, i, n = [], 0, len(body)
    while i < n:
        fm = re.compile(r"\s*,?\s*([A-Za-z_][\w\-]*)\s*=\s*").match(body, i)
        if not fm:
            break
        name, i = fm.group(1).lower(), fm.end()
        if i < n and body[i] == "{":
            depth, start = 0, i
            while i < n:
                if body[i] == "{":
                    depth += 1
                elif body[i] == "}":
                    depth -= 1
                    if depth == 0:
                        i += 1
                        break
                i += 1
            value = body[start:i]
        elif i < n and body[i] == '"':
            start = i
            i += 1
            while i < n and body[i] != '"':
                i += 2 if body[i] == "\\" else 1
            i += 1
            value = body[start:i]
        else:
            vm = re.compile(r"[^,}]*").match(body, i)
            value, i = vm.group(0).strip(), vm.end()
        fields.append((name, value))
    return etype, key, fields


def unwrap(value):
    v = value.strip()
    if (v.startswith("{") and v.endswith("}")) or (v.startswith('"') and v.endswith('"')):
        v = v[1:-1]
    return v.strip()


def read_existing(bib_text):
    dois, titles, keys = set(), set(), set()
    for raw in split_entries(bib_text):
        parsed = parse_entry(raw)
        if not parsed:
            continue
        _, key, fields = parsed
        keys.add(key.lower())
        f = dict(fields)
        if "doi" in f:
            dois.add(normalize_doi(unwrap(f["doi"])))
        if "title" in f:
            titles.add(normalize_title(unwrap(f["title"])))
    return dois, titles, keys


# --------------------------------------------------------------------------- #
# ORCID
# --------------------------------------------------------------------------- #


def orcid_works(orcid_id):
    url = f"https://pub.orcid.org/v3.0/{orcid_id}/works"
    data = json.loads(http_get(url, "application/json"))
    works = []
    for group in data.get("group", []):
        summaries = group.get("work-summary") or []
        if not summaries:
            continue
        s = summaries[0]  # ORCID's preferred version of this work
        ids = (group.get("external-ids") or {}).get("external-id") or []
        doi = ""
        for ext in sorted(ids, key=lambda e: e.get("external-id-relationship") != "self"):
            if (ext.get("external-id-type") or "").lower() == "doi":
                doi = normalize_doi(ext.get("external-id-value"))
                break
        title = (((s.get("title") or {}).get("title")) or {}).get("value", "")
        year = ((((s.get("publication-date") or {}).get("year")) or {}).get("value")) or ""
        works.append({"doi": doi, "title": title, "type": s.get("type", ""), "year": year})
    return works


def fetch_bibtex(doi):
    quoted = urllib.parse.quote(doi, safe="/")
    try:
        return http_get(f"https://doi.org/{quoted}", "application/x-bibtex; charset=utf-8")
    except RuntimeError as first:
        url = f"https://api.crossref.org/works/{quoted}/transform/application/x-bibtex"
        if CROSSREF_MAILTO:
            url += f"?mailto={urllib.parse.quote(CROSSREF_MAILTO)}"
        try:
            return http_get(url, "application/x-bibtex")
        except RuntimeError:
            raise first


# --------------------------------------------------------------------------- #
# Turning a downloaded record into an al-folio entry
# --------------------------------------------------------------------------- #

STOPWORDS = {"of", "the", "and", "for", "in", "on", "&", "a", "an", "to", "at"}


def journal_abbr(journal):
    if not journal:
        return ""
    name = re.sub(r"[{}\\]", "", journal).strip()
    if name.lower() in JOURNAL_ABBR:
        return JOURNAL_ABBR[name.lower()]
    words = [w for w in re.split(r"[\s\-:/]+", name) if w and w.lower() not in STOPWORDS]
    initials = "".join(w[0].upper() for w in words if w[0].isalnum())
    return initials or name[:10]


def make_key(fields, existing_keys):
    f = dict(fields)
    author = unwrap(f.get("author", ""))
    first = author.split(" and ")[0].strip()
    last = first.split(",")[0] if "," in first else (first.split()[-1] if first.split() else "")
    year = re.sub(r"\D", "", unwrap(f.get("year", "")))[:4]
    words = [w for w in re.findall(r"[A-Za-z]+", unwrap(f.get("title", ""))) if w.lower() not in STOPWORDS]
    base = f"{ascii_slug(last) or 'paper'}{year}{ascii_slug(words[0]) if words else ''}"
    key, n = base, 1
    while key.lower() in existing_keys:
        n += 1
        key = f"{base}{chr(ord('a') + n - 2)}"
    existing_keys.add(key.lower())
    return key


def build_entry(raw_bibtex, doi, existing_keys):
    parsed = parse_entry(raw_bibtex.strip())
    if not parsed:
        raise ValueError("could not parse BibTeX returned for this DOI")
    etype, _, fields = parsed
    names = [n for n, _ in fields]
    f = dict(fields)

    out = []
    abbr = journal_abbr(html.unescape(unwrap(f.get("journal", f.get("booktitle", "")))))
    if abbr:
        out.append(("abbr", "{" + abbr + "}"))
    for name, value in fields:
        if name in ("abbr",):
            continue
        value = html.unescape(value)  # Crossref sometimes sends "&amp;" etc.
        if name == "url" and "doi.org/" in value:
            continue  # duplicate of the html link added below
        if name == "doi":
            value = "{" + doi + "}"  # clean, bare DOI
        elif not value.startswith(("{", '"')):
            value = value if value.isdigit() or name == "month" else "{" + value + "}"
        out.append((name, value))
    if "doi" not in names:
        out.append(("doi", "{" + doi + "}"))
    out.append(("html", "{https://doi.org/" + doi + "}"))
    out.append(("altmetric", "{true}"))
    out.append(("bibtex_show", "{true}"))

    key = make_key(fields, existing_keys)
    width = max(len(n) for n, _ in out)
    lines = [f"@{etype}{{{key},"]
    lines += [f"  {n.ljust(width)} = {v}," for n, v in out]
    lines[-1] = lines[-1][:-1]  # no comma after the last field
    lines.append("}")
    return "\n".join(lines)


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #


def load_ignore(path):
    if not os.path.exists(path):
        return set()
    with open(path, encoding="utf-8") as fh:
        return {normalize_doi(l.split("#")[0]) for l in fh if l.split("#")[0].strip()}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true", help="show what would be added without changing papers.bib")
    args = ap.parse_args()

    with open(BIB_FILE, encoding="utf-8") as fh:
        bib_text = fh.read()
    have_dois, have_titles, have_keys = read_existing(bib_text)
    ignored = load_ignore(IGNORE_FILE)

    print(f"ORCID {ORCID_ID}: fetching works...")
    works = orcid_works(ORCID_ID)
    print(f"  {len(works)} works on ORCID, {len(have_dois)} DOIs already in {BIB_FILE}")

    new_entries, notes = [], []
    for w in works:
        label = f"{w['title'][:70]!r} ({w['year'] or 'n.d.'})"
        if w["type"] and INCLUDE_TYPES and w["type"] not in INCLUDE_TYPES:
            notes.append(f"skip  {label}: type '{w['type']}' not imported")
            continue
        if not w["doi"]:
            notes.append(f"skip  {label}: no DOI on ORCID, add it to papers.bib by hand")
            continue
        if w["doi"] in ignored:
            continue
        if w["doi"] in have_dois or normalize_title(w["title"]) in have_titles:
            continue
        try:
            entry = build_entry(fetch_bibtex(w["doi"]), w["doi"], have_keys)
        except Exception as e:
            notes.append(f"error {label}: {e}")
            continue
        new_entries.append(entry)
        have_dois.add(w["doi"])
        notes.append(f"add   {label}: doi {w['doi']}")

    for n in notes:
        print("  " + n)

    if not new_entries:
        print("No new publications to add.")
        return 0

    if args.dry_run:
        print(f"\n--dry-run: would add {len(new_entries)} entr{'y' if len(new_entries) == 1 else 'ies'}:\n")
        print("\n\n".join(new_entries))
        return 0

    with open(BIB_FILE, "a", encoding="utf-8") as fh:
        fh.write(("" if bib_text.endswith("\n") else "\n") + "\n" + "\n\n".join(new_entries) + "\n")
    print(f"Added {len(new_entries)} entr{'y' if len(new_entries) == 1 else 'ies'} to {BIB_FILE}.")
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as fh:
            fh.write(f"Added {len(new_entries)} publication(s) from ORCID:\n\n")
            for n in notes:
                if n.startswith("add"):
                    fh.write(f"- {n[6:]}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
