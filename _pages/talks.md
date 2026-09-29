---
layout: page
permalink: /talks/
title: talks
nav: true
nav_order: 4
description: Conference papers, presentations, posters, and workshops, newest first.
---

{% comment %}
  Items come from _data/talks.yml. Grouped by category, then by year (newest first),
  with year labels styled like the publications page.
{% endcomment %}

<div class="publications talks">
{% assign cats = "Conference Papers,Presentations,Workshops & Reports" | split: "," %}
{% for cat in cats %}
{% assign items = site.data.talks | where: "category", cat | sort: "date" | reverse %}
{% if items.size > 0 %}
<h2 class="talks-category">{{ cat }}</h2>
{% assign years = items | group_by_exp: "t", "t.date | date: '%Y'" %}
{% for y in years %}
<h2 class="bibliography">{{ y.name }}</h2>
<ul>
{% for t in y.items %}
  <li style="margin-bottom: 0.9rem;">
    <strong>{{ t.title }}</strong>{% if t.type %} &nbsp;<span style="opacity: 0.7;">[{{ t.type }}]</span>{% endif %}{% if t.award %} &nbsp;<span style="color: var(--global-theme-color);">★ {{ t.award }}</span>{% endif %}<br>
    {% if t.authors %}{{ t.authors | replace: 'K. Maynor', '<strong>K. Maynor</strong>' }}<br>{% endif %}
    <em>{{ t.venue }}</em>{% if t.location %}, {{ t.location }}{% endif %} &middot; {% if t.date_text %}{{ t.date_text }}{% else %}{{ t.date | date: "%B %Y" }}{% endif %}
    {% if t.slides %} &middot; <a href="{{ t.slides | relative_url }}">Slides</a>{% endif %}
    {% if t.link %} &middot; <a href="{{ t.link }}">Link</a>{% endif %}
    {% if t.doi %} &middot; <a href="https://doi.org/{{ t.doi }}">DOI</a>{% endif %}
  </li>
{% endfor %}
</ul>
{% endfor %}
{% endif %}
{% endfor %}
</div>

<style>
  .talks { margin-top: 0; }
  .talks h2.talks-category { margin-top: 2.5rem; margin-bottom: 0; }
  .talks h2.talks-category:first-child { margin-top: 0; }
  .talks h2.bibliography { margin-top: 1rem; font-size: 1.6rem; }
  .talks ul { padding-left: 1.25rem; }
</style>
