---
layout: page
permalink: /publications/conferences/
title: conference papers
nav: false
---

<!-- Listed under the "publications" dropdown (see children: in _pages/publications.md) -->

{% include bib_search.liquid %}

<div class="publications">

{% bibliography --query @inproceedings %}

</div>

<style>
  /* "Certificate" button inside award panels — same look as the teaching page */
  .cert-btn { display: inline-block; margin-left: .4rem; padding: .05rem .5rem; font-size: .75rem;
    border: 1px solid var(--global-theme-color); border-radius: 4px; vertical-align: middle;
    color: var(--global-theme-color); text-decoration: none; }
  .cert-btn:hover { text-decoration: none; background: var(--global-theme-color); color: var(--global-bg-color) !important; }
  .cert-btn i { font-size: .75rem; }
</style>
