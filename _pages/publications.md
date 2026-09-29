---
layout: page
permalink: /publications/
title: publications
description: Journal articles and conference papers, newest first.
nav: true
dropdown: true
children:
  - title: journal articles
    permalink: /publications/journals/
  - title: conference papers
    permalink: /publications/conferences/
nav_order: 2
---

<!-- _pages/publications.md -->

<!-- Bibsearch Feature -->

{% include bib_search.liquid %}

<div class="publications">

<div class="pub-section">Journal Articles</div>
{% bibliography --query @article %}

<div class="pub-section">Conference Papers</div>
{% bibliography --query @inproceedings %}

</div>

<style>
  /* Section labels styled like the teaching and talks pages */
  .pub-section { margin: 2.5rem 0 .5rem; display: flex; align-items: center; gap: .6rem;
    font-size: .8rem; font-weight: 600; letter-spacing: .12em; text-transform: uppercase;
    color: var(--global-theme-color); text-decoration: none; }
  .pub-section:first-child { margin-top: .5rem; }
  .pub-section::after { content: ""; flex: 1; height: 1px; background: var(--global-divider-color); }
</style>

<style>
  /* "Certificate" button inside award panels — same look as the teaching page */
  .cert-btn { display: inline-block; margin-left: .4rem; padding: .05rem .5rem; font-size: .75rem;
    border: 1px solid var(--global-theme-color); border-radius: 4px; vertical-align: middle;
    color: var(--global-theme-color); text-decoration: none; }
  .cert-btn:hover { text-decoration: none; background: var(--global-theme-color); color: var(--global-bg-color) !important; }
  .cert-btn i { font-size: .75rem; }
</style>
