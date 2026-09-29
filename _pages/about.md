---
layout: about
title: about
permalink: /
subtitle: >
  Postdoctoral Fellow | <a href='https://amenonlab.me.gatech.edu/'>Water-Energy Research Laboratory (WERL)</a><br> 
  George W. Woodruff School of Mechanical Engineering | Georgia Institute of Technology

profile:
  align: right
  image: profile_photo.jpg
  image_circular: false # crops the image to make it circular
  more_info: #

selected_papers: true # includes a list of papers marked as "selected={true}"
social: true # includes social icons at the bottom of the page

announcements:
  enabled: true # includes a list of news items
  scrollable: true # adds a vertical scroll bar if there are more than 3 news items
  limit: 5 # leave blank to include all the news in the `_news` folder

latest_posts:
  enabled: false
  scrollable: true # adds a vertical scroll bar if there are more than 3 new posts items
  limit: 3 # leave blank to include all the blog posts
---

I am a Postdoctoral Fellow in the [Water-Energy Research Laboratory (WERL)](https://amenonlab.me.gatech.edu/) in the [George W. Woodruff School of Mechanical Engineering](https://www.me.gatech.edu/) at Georgia Institute of Technology (Georgia Tech). My research sits at the intersection of water, energy, and carbon management. At WERL, I study desalination systems for water production and brine concentration.

I received my PhD in Mechanical Engineering from the [Walker Department of Mechanical Engineering](https://me.utexas.edu/) at The University of Texas at Austin in 2026, working in the [Bahadur Research Group](https://bahadurlab.me.utexas.edu/) as a **National Science Foundation Graduate Research Fellow**. My doctoral research focused on enhancing heat and mass transport for carbon dioxide direct air capture and clathrate hydrate-based carbon sequestration and desalination. My work spanned fundamental experiments and materials characterization through process intensification, system-level modeling, and techno-economic and life cycle analyses. Along the way, I also worked on clean hydrogen pathways for ammonia and bioethanol production, and on thermal management for power transformers and next-generation electronics packaging.

Before graduate school, I spent four years as a Test Engineer at [Heat Transfer Research, Inc. (HTRI)](https://www.htri.net/), running pilot-scale heat transfer experiments and leading the company's ISO 17025 quality program and safety program. I received my B.S. in Chemical Engineering from the [Artie McFerrin Department of Chemical Engineering](https://engineering.tamu.edu/chemical/index.html) at Texas A&M University - College Station.

Outside of research, I enjoy cooking, hiking, playing tennis, and traveling.

**Areas of research interest:** desalination and brine management · carbon capture, utilization & storage · gas hydrates · direct air capture · thermal and energy systems · techno-economic and life cycle analysis · low-carbon hydrogen

<style>
  /* Brand colors for the social icons on the home page */
  .social .contact-icons a i::before { transition: color .2s ease, opacity .2s ease; }
  .social .contact-icons a .fa-linkedin::before       { color: #0A66C2; } /* LinkedIn blue */
  .social .contact-icons a .ai-google-scholar::before { color: #4285F4; } /* Google Scholar blue */
  .social .contact-icons a .ai-orcid::before          { color: #A6CE39; } /* ORCID green */
  .social .contact-icons a .fa-envelope::before,
  .social .contact-icons a .ai-cv::before             { color: var(--global-theme-color); } /* no brand color: use site accent */
  .social .contact-icons a:hover i::before            { opacity: .75; }
  /* Slightly brighter versions so they stay readable in dark mode */
  html[data-theme="dark"] .social .contact-icons a .fa-linkedin::before       { color: #4C9BE8; }
  html[data-theme="dark"] .social .contact-icons a .ai-google-scholar::before { color: #7BAAF7; }
    /* Smaller social icons (theme default is 4rem) */
  .social .contact-icons { font-size: 2rem; }
  .social .contact-icons a { margin: 0 .15rem; }
    .post article > .clearfix p { text-align: justify; hyphens: auto; -webkit-hyphens: auto; }
  @media (min-width: 576px) {
    .post .profile.float-right { margin-left: 2.25rem; margin-bottom: 1.5rem; }
    .post .profile.float-left  { margin-right: 2.25rem; margin-bottom: 1.5rem; }
  }
</style>

<script>
  // Custom hover text for the Scholar and ORCID icons (the theme doesn't let you set these directly).
  document.addEventListener("DOMContentLoaded", function () {
    var hover = {
      "scholar.google.com": "Google Scholar profile",
      "orcid.org": "ORCID profile"
    };
    document.querySelectorAll(".contact-icons a, .navbar-brand.social a").forEach(function (a) {
      for (var site in hover) {
        if (a.href.indexOf(site) !== -1) a.title = hover[site];
      }
    });
  });
</script>
