---
layout: page
title: research
permalink: /research/
description:
nav: true
nav_order: 3
---

{% comment %}
  Each theme = heading, one paragraph, a figure row, and a short list of related publications.
  Figures live in assets/img/research/. In a figure row, set each figure's flex value to the
  image's width/height ratio so side-by-side images line up at the same height.
{% endcomment %}

<style>
  .rs-intro { font-size: 1.08rem; line-height: 1.7; margin-bottom: 2rem; }
  .rs-theme { scroll-margin-top: 5rem; }
  .rs-theme h2 { font-size: 1.5rem; font-weight: 600; margin: 0 0 .9rem; }
  .rs-theme p { line-height: 1.7; }
  .rs-figs { display: flex; gap: 1rem; align-items: flex-start; margin: 1.25rem 0 1rem; }
  .rs-figs figure { margin: 0; min-width: 0; }
  .rs-figs img { width: 100%; height: auto; display: block; background: #fff;
    border: 1px solid var(--global-divider-color); border-radius: 6px; }
  .rs-figs figcaption { font-size: .8rem; color: var(--global-text-color-light); margin-top: .4rem; line-height: 1.4; }
  .rs-pubs { font-size: .88rem; color: var(--global-text-color-light); margin: 0; }
  .rs-pubs strong { font-weight: 600; color: var(--global-text-color); }
  .rs-pubs ul { margin: .25rem 0 0; padding-left: 1.1rem; }
  .rs-pubs li { margin-bottom: .15rem; }
  hr.rs-divider { margin: 2.5rem 0; border: 0; border-top: 1px solid var(--global-divider-color); }
  @media (max-width: 575.98px) { .rs-figs { flex-direction: column; } }
  .rs-intro { font-size: 1.08rem; line-height: 1.7; margin-bottom: 2rem; text-align: justify; hyphens: auto; }
  .rs-theme p { line-height: 1.7; text-align: justify; hyphens: auto; }
</style>

<p class="rs-intro">My research sits at the intersection of thermal–fluid engineering and techno-economics. I pair experiments and process models with cost and life-cycle analysis to find where new energy, water, and carbon technologies can realistically compete. The common thread is the energy–water–carbon nexus: how decarbonization, clean fuels, and the rapid growth of data centers are creating new demands on heat management, water supply, and energy infrastructure.</p>

<section class="rs-theme" id="carbon-capture">
<h2>CARBON CAPTURE AND STORAGE WITH CO₂ HYDRATES</h2>
<p>Removing carbon dioxide at the scale climate targets require will take options beyond today's solvent-based capture systems. CO₂ hydrates, ice-like solids that trap CO₂ inside cages of water molecules, offer an alternative that uses only water: they can separate CO₂ from other gases and remain stable on the cold, high-pressure seafloor for permanent storage. Their practical barrier has always been speed. My work addresses that barrier by forming hydrates in seconds from impure, flue-gas-like streams and seawater without chemical additives, and by assessing where hydrate-based capture fits alongside established technologies on performance, cost, and life-cycle impact. I am now extending these ideas to direct air capture, asking what it would take for compact, engineered-surface contactors to become economically competitive.</p>
<div class="rs-figs">
<figure style="flex: 1"><img src="{{ '/assets/img/research/co2-nucleation.jpg' | relative_url }}" alt="High-speed images of CO2 hydrate nucleating at the gas–liquid interface and growing through the water" data-zoomable loading="lazy"><figcaption>CO₂ hydrate nucleating and growing in seconds from a CO₂/N₂ gas mixture. <em>Maynor et al., Int. J. Greenh. Gas Control, 2026.</em></figcaption></figure>
</div>
<div class="rs-pubs"><strong>Related publications</strong>
<ul>
<li><a href="https://doi.org/10.1016/j.ijggc.2026.104751" target="_blank">Ultrafast formation of CO₂ hydrates from CO₂ and N₂ mixtures</a>, <em>Int. J. Greenh. Gas Control</em> (2026)</li>
<li><a href="https://doi.org/10.1016/j.jece.2026.124335" target="_blank">Review of clathrate hydrate-based CO₂ capture</a>, <em>J. Environ. Chem. Eng.</em> (2026)</li>
<li><a href="https://doi.org/10.1021/acs.langmuir.4c02882" target="_blank">Magnesium-induced rapid nucleation of hydrates</a>, <em>Langmuir</em> (2024)</li>
<li><a href="{{ '/publications/conferences/' | relative_url }}">Hydrate-based carbon capture from CO₂/N₂ mixtures</a>, <em>ASME Energy Sustainability</em> (2025)</li>
</ul></div>
</section>

<hr class="rs-divider">

<section class="rs-theme" id="water">
<h2>DESALINATION TO MEET GROWING WATER DEMANDS</h2>
<p>Water is becoming a constraint on the energy transition. In Texas, the growth of data centers is set to multiply their water demand within a few years, competing with cities, agriculture, and industry. I work on both sides of this problem: quantifying how much water data centers will need, both directly for cooling and indirectly through the electricity they consume, and evaluating new supplies from non-conventional sources such as oilfield produced water. Hydrate-based desalination, which uses CO₂ hydrates to pull fresh water out of brine, is one such pathway. My techno-economic analysis identifies where it could compete and which parts of the process must improve to get there.</p>
<div class="rs-figs">
<figure style="flex: 1.76"><img src="{{ '/assets/img/research/desal-process.jpg' | relative_url }}" alt="Process flow diagram of hydrate-based desalination using CO2 hydrates" data-zoomable loading="lazy"><figcaption>Hydrate-based desalination process for treating produced water. <em>Maynor &amp; Bahadur, in preparation.</em></figcaption></figure>
<figure style="flex: 1.87"><img src="{{ '/assets/img/research/dc-water.jpg' | relative_url }}" alt="Projected total water use by Texas data centers in 2030 and 2040 under several capacity scenarios" data-zoomable loading="lazy"><figcaption>Projected Texas data-center water use, 2030 and 2040. <em>Arzumanyan et al., BEG white paper, 2025.</em></figcaption></figure>
</div>
<div class="rs-pubs"><strong>Related publications</strong>
<ul>
<li><a href="https://compass.beg.utexas.edu/" target="_blank">Water use requirements for data centers in Texas</a>, white paper, Bureau of Economic Geology (2025)</li>
<li>Hydrate-based desalination for providing water to data centers (in preparation)</li>
</ul></div>
</section>

<hr class="rs-divider">

<section class="rs-theme" id="fuels">
<h2>LOW-CARBON HYDROGEN SUPPLY CHAIN - FROM HYDROGEN TO BIOFUELS</h2>
<p>Clean hydrogen is only as valuable as the products it enables. Rather than evaluating hydrogen in isolation, I follow it through real supply chains to see where its cost and emissions benefits end up. This includes process modeling and techno-economic analysis of ammonia production from low-carbon hydrogen in the Permian Basin, and tracing green hydrogen through fertilizer, corn, and ethanol in the U.S. Midwest. The results identify the hydrogen prices and policies at which low-carbon fuels and chemicals become viable, and show how decarbonizing one link can lower emissions across an entire value chain.</p>
<div class="rs-figs">
<figure style="flex: 1.33"><img src="{{ '/assets/img/research/h2-value-chain.jpg' | relative_url }}" alt="Value chain of green hydrogen: hydrogen to ammonia fertilizer to corn to ethanol" data-zoomable loading="lazy"><figcaption>Following green hydrogen from production to ethanol. <em>Maynor et al., Sustain. Energy Technol. Assess., 2026.</em></figcaption></figure>
<figure style="flex: 1.26"><img src="{{ '/assets/img/research/nh3-lcoa.jpg' | relative_url }}" alt="Levelized cost of ammonia versus hydrogen cost for three plant energy cases" data-zoomable loading="lazy"><figcaption>Ammonia cost as a function of hydrogen price. <em>Maynor et al., ASME Energy Sustainability, 2025.</em></figcaption></figure>
</div>
<div class="rs-pubs"><strong>Related publications</strong>
<ul>
<li><a href="https://doi.org/10.1016/j.seta.2026.104911" target="_blank">Levelized cost pass-through of green hydrogen in the bioethanol value chain</a>, <em>Sustain. Energy Technol. Assess.</em> (2026)</li>
<li><a href="{{ '/publications/conferences/' | relative_url }}">Ammonia production from clean hydrogen in the Permian Basin</a>, <em>ASME Energy Sustainability</em> (2025)</li>
</ul></div>
</section>

<hr class="rs-divider">

<section class="rs-theme" id="transformers">
<h2>THERMAL MANAGEMENT - FROM CHIP TO GRID</h2>
<p>The electric grid depends on power transformers, and many are due for replacement just as electricity demand is rising. A transformer's lifetime is set by its paper insulation, which degrades faster the hotter it runs. In collaborative work, we combine thermal modeling with accelerated aging experiments to show how insulation paper with higher thermal conductivity, and alternative ester-based coolants, can keep windings cooler and substantially extend transformer life. This offers a lower-cost path to a more reliable grid than wholesale replacement.</p>
<div class="rs-figs">
<figure style="flex: 1.53"><img src="{{ '/assets/img/research/xfmr-model.jpg' | relative_url }}" alt="Model geometry of a distribution transformer showing core, windings and insulation layers" data-zoomable loading="lazy"><figcaption>Thermal model of a distribution transformer. <em>Bilyaz et al., Heliyon, 2024.</em></figcaption></figure>
<figure style="flex: 1.28"><img src="{{ '/assets/img/research/xfmr-hotspot.jpg' | relative_url }}" alt="Maximum winding temperature decreasing as insulation paper thermal conductivity increases" data-zoomable loading="lazy"><figcaption>Hot-spot temperature falls as paper conductivity rises. <em>Bilyaz et al., Heliyon, 2024.</em></figcaption></figure>
</div>
<div class="rs-pubs"><strong>Related publications</strong>
<ul>
<li><a href="https://doi.org/10.1016/j.heliyon.2024.e27783" target="_blank">Impact of high thermal conductivity paper on the performance and life of power transformers</a>, <em>Heliyon</em> (2024)</li>
<li>Accelerated thermal aging and life estimation of transformer insulation paper in ester oil (under review)</li>
</ul></div>
</section>
