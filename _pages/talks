---
layout: page
permalink: /talks/
title: talks
nav: true
nav_order: 4
description: Conference presentations, invited talks, posters, and conference papers.
---

{% assign items = site.data.talks | sort: "date" | reverse %}
{% assign grouped = items | group_by_exp: "item", "item.date | date: '%Y'" %}

{% for group in grouped %}
<h2>{{ group.name }}</h2>
<ul>
{% for t in group.items %}
  <li style="margin-bottom: 0.9rem;">
    <strong>{{ t.title }}</strong>{% if t.award %} &nbsp;<span style="color: var(--global-theme-color);">★ {{ t.award }}</span>{% endif %}<br>
    {% if t.authors %}{{ t.authors }}<br>{% endif %}
    <em>{{ t.venue }}</em>{% if t.location %}, {{ t.location }}{% endif %} &middot; {{ t.date | date: "%B %Y" }}{% if t.type %} &middot; {{ t.type }}{% endif %}
    {% if t.slides %} &middot; <a href="{{ t.slides | relative_url }}">Slides</a>{% endif %}
    {% if t.link %} &middot; <a href="{{ t.link }}">Link</a>{% endif %}
    {% if t.doi %} &middot; <a href="https://doi.org/{{ t.doi }}">DOI</a>{% endif %}
  </li>
{% endfor %}
</ul>
{% endfor %}
