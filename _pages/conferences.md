---
layout: page
permalink: /conferences/
title: conferences
nav: true
nav_order: 4
description: Conferences where I've shared this work — talks, posters, and papers.
---

A running record of the conferences where I've presented my research — talks, posters, and papers — and a few moments from the road.

{% assign events = site.data.conferences | sort: "date" | reverse %}
{% for e in events %}
<div style="margin-bottom: 1.8rem;">
  <h2 style="margin-bottom: 0.15rem;">{{ e.name }}</h2>
  <p style="color: var(--global-text-color-light); margin-top: 0; margin-bottom: 0.5rem;">
    {% if e.location %}{{ e.location }} &middot; {% endif %}{% if e.date_text %}{{ e.date_text }}{% else %}{{ e.date | date: "%B %Y" }}{% endif %}{% if e.role %} &middot; {{ e.role }}{% endif %}
  </p>
  {% if e.image %}<img src="{{ e.image | relative_url }}" alt="{{ e.name }}" style="max-width: 440px; width: 100%; border-radius: 8px; margin: 0.2rem 0 0.6rem;">{% endif %}
  {% if e.note %}<p><em>{{ e.note }}</em></p>{% endif %}
  {% if e.items %}
  <ul>
    {% for it in e.items %}
    <li style="margin-bottom: 0.45rem;">
      {{ it.title }} <span style="opacity: 0.7;">[{{ it.type }}]</span>{% if it.award %} &nbsp;<span style="color: var(--global-theme-color);">★ {{ it.award }}</span>{% endif %}
      {% if it.authors %}<br><span style="color: var(--global-text-color-light); font-size: 0.9em;">{{ it.authors | replace: 'K. Maynor', '<strong>K. Maynor</strong>' }}</span>{% endif %}
    </li>
    {% endfor %}
  </ul>
  {% endif %}
</div>
{% endfor %}
