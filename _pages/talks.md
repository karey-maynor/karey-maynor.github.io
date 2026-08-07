---
layout: page
permalink: /talks/
title: talks
nav: true
nav_order: 4
description: Conference papers, presentations, posters, and workshops.
---

{% assign cats = "Conference Papers,Presentations,Workshops & Reports" | split: "," %}
{% for cat in cats %}
{% assign items = site.data.talks | where: "category", cat | sort: "date" | reverse %}
{% if items.size > 0 %}
<h2>{{ cat }}</h2>
<ul>
{% for t in items %}
  <li style="margin-bottom: 0.9rem;">
    <strong>{{ t.title }}</strong>{% if t.type %} &nbsp;<span style="opacity: 0.7;">[{{ t.type }}]</span>{% endif %}{% if t.award %} &nbsp;<span style="color: var(--global-theme-color);">★ {{ t.award }}</span>{% endif %}<br>
    {% if t.authors %}{{ t.authors }}<br>{% endif %}
    <em>{{ t.venue }}</em>{% if t.location %}, {{ t.location }}{% endif %} &middot; {% if t.date_text %}{{ t.date_text }}{% else %}{{ t.date | date: "%B %Y" }}{% endif %}
    {% if t.slides %} &middot; <a href="{{ t.slides | relative_url }}">Slides</a>{% endif %}
    {% if t.link %} &middot; <a href="{{ t.link }}">Link</a>{% endif %}
    {% if t.doi %} &middot; <a href="https://doi.org/{{ t.doi }}">DOI</a>{% endif %}
  </li>
{% endfor %}
</ul>
{% endif %}
{% endfor %}
