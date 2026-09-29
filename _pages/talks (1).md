---
layout: page
permalink: /talks/
title: talks
nav: true
nav_order: 4
description: Presentations, posters, invited seminars, workshops, and reports, newest first.
---

{% comment %}
  Items come from _data/talks.yml. Each category gets its own outlined card (same style as
  the teaching page); inside, items are grouped by year, newest first.
  Conference papers live in _bibliography/papers.bib and show under publications → conference papers.
{% endcomment %}

<style>
  .tlk-section { margin: 2.25rem 0 1rem; display: flex; align-items: center; gap: .6rem;
    font-size: .8rem; font-weight: 600; letter-spacing: .12em; text-transform: uppercase;
    color: var(--global-theme-color); }
  .tlk-section:first-of-type { margin-top: .5rem; }
  .tlk-section::after { content: ""; flex: 1; height: 1px; background: var(--global-divider-color); }
  .tlk-card { padding: .4rem 1.5rem; margin-bottom: 1rem;
    background: var(--global-card-bg-color); border: 1px solid var(--global-divider-color);
    border-left: 3px solid var(--global-theme-color); border-radius: 8px; }
  .tlk-year { display: flex; gap: 1.5rem; padding: 1rem 0; border-bottom: 1px solid var(--global-divider-color); }
  .tlk-year:last-child { border-bottom: 0; }
  .tlk-when { flex: 0 0 4rem; font-size: .95rem; font-weight: 600; color: var(--global-text-color); }
  .tlk-items { flex: 1; min-width: 0; }
  .tlk-item { margin-bottom: 1rem; }
  .tlk-item:last-child { margin-bottom: 0; }
  .tlk-title { font-size: 1rem; font-weight: 600; color: var(--global-text-color); line-height: 1.4; }
  .tlk-authors { font-size: .9rem; margin-top: .15rem; }
  .tlk-authors strong { font-weight: 700; }
  .tlk-venue { font-size: .9rem; color: var(--global-text-color-light); margin-top: .1rem; }
  .tlk-tags { display: flex; flex-wrap: wrap; gap: .4rem; margin-top: .4rem; }
  .tlk-type { font-size: .72rem; padding: .05rem .55rem; border-radius: 4px;
    border: 1px solid var(--global-theme-color); color: var(--global-theme-color); }
  .tlk-award { font-size: .72rem; padding: .05rem .55rem; border-radius: 4px; font-weight: 600;
    background: var(--global-theme-color); color: var(--global-bg-color); }
  .tlk-links a { font-size: .85rem; }
  @media (max-width: 575.98px) {
    .tlk-card { padding: .2rem 1rem; }
    .tlk-year { flex-direction: column; gap: .5rem; }
    .tlk-when { flex: none; }
  }
</style>

{% assign cats = "Presentations,Workshops & Reports" | split: "," %}
{% for cat in cats %}
{% assign items = site.data.talks | where: "category", cat | sort: "date" | reverse %}
{% if items.size > 0 %}
<div class="tlk-section">{{ cat }}</div>
<div class="tlk-card">
{% assign years = items | group_by_exp: "t", "t.date | date: '%Y'" %}
{% for y in years %}
  <div class="tlk-year">
    <div class="tlk-when">{{ y.name }}</div>
    <div class="tlk-items">
    {% for t in y.items %}
      <div class="tlk-item">
        <div class="tlk-title">{{ t.title }}</div>
        {% if t.authors %}<div class="tlk-authors">{{ t.authors | replace: 'K. Maynor', '<strong>K. Maynor</strong>' }}</div>{% endif %}
        <div class="tlk-venue"><em>{{ t.venue }}</em>{% if t.location %}, {{ t.location }}{% endif %} &middot; {% if t.date_text %}{{ t.date_text }}{% else %}{{ t.date | date: "%B %Y" }}{% endif %}<span class="tlk-links">{% if t.slides %} &middot; <a href="{{ t.slides | relative_url }}">Slides</a>{% endif %}{% if t.link %} &middot; <a href="{{ t.link }}">Link</a>{% endif %}{% if t.doi %} &middot; <a href="https://doi.org/{{ t.doi }}">DOI</a>{% endif %}</span></div>
        {% if t.type or t.award %}<div class="tlk-tags">{% if t.type %}<span class="tlk-type">{{ t.type }}</span>{% endif %}{% if t.award %}<span class="tlk-award">★ {{ t.award }}</span>{% endif %}</div>{% endif %}
      </div>
    {% endfor %}
    </div>
  </div>
{% endfor %}
</div>
{% endif %}
{% endfor %}
