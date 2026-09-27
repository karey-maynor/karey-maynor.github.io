---
layout: page
permalink: /teaching/
title: teaching
description: Training in teaching and pedagogy, and experience in the lab and classroom.
nav: true
nav_order: 6
---

<style>
  .tch-section { margin: 2.25rem 0 1rem; display: flex; align-items: center; gap: .6rem;
    font-size: .8rem; font-weight: 600; letter-spacing: .12em; text-transform: uppercase;
    color: var(--global-theme-color); }
  .tch-section::after { content: ""; flex: 1; height: 1px; background: var(--global-divider-color); }
  .tch-card { display: flex; gap: 1.5rem; padding: 1.25rem 1.5rem; margin-bottom: 1rem;
    background: var(--global-card-bg-color); border: 1px solid var(--global-divider-color);
    border-left: 3px solid var(--global-theme-color); border-radius: 8px; }
  .tch-when { flex: 0 0 8.5rem; font-size: .8rem; color: var(--global-text-color-light); line-height: 1.5; }
  .tch-when strong { display: block; font-size: .95rem; color: var(--global-text-color); }
  .tch-body { flex: 1; min-width: 0; }
  .tch-role { margin: 0; font-size: 1.1rem; font-weight: 600; color: var(--global-text-color); }
  .tch-org { margin: .15rem 0 .6rem; font-size: .9rem; color: var(--global-text-color-light); }
  .tch-org i { color: var(--global-theme-color); margin-right: .3rem; }
  .tch-course { display: inline-block; margin-bottom: .5rem; padding: .15rem .6rem; border-radius: 4px;
    font-size: .85rem; font-weight: 600; color: var(--global-theme-color);
    border: 1px solid var(--global-theme-color); }
  .tch-body p { margin-bottom: .6rem; }
  .tch-tags { display: flex; flex-wrap: wrap; gap: .4rem; margin-top: .4rem; }
  .tch-tags span { font-size: .75rem; padding: .15rem .6rem; border-radius: 999px;
    background: var(--global-divider-color); color: var(--global-text-color); }
  .tch-stats { display: flex; flex-wrap: wrap; gap: .75rem; margin-top: .8rem; }
  .tch-stat { flex: 1 1 6rem; text-align: center; padding: .6rem .5rem; border-radius: 6px;
    border: 1px solid var(--global-divider-color); }
  .tch-stat b { display: block; font-size: 1.6rem; line-height: 1.1; color: var(--global-theme-color); }
  .tch-stat small { font-size: .75rem; color: var(--global-text-color-light); }
  .tch-certs { list-style: none; padding: 0; margin: 0; }
  .tch-certs li { display: flex; gap: .75rem; align-items: flex-start; padding: .75rem 0;
    border-bottom: 1px solid var(--global-divider-color); }
  .tch-certs li:last-child { border-bottom: 0; }
  .tch-certs i { color: var(--global-theme-color); font-size: 1.1rem; margin-top: .2rem; }
  .tch-certs span { display: block; font-size: .85rem; color: var(--global-text-color-light); }
  @media (max-width: 575.98px) {
    .tch-card { flex-direction: column; gap: .5rem; padding: 1rem 1.1rem; }
    .tch-when { flex: none; }
    .tch-when strong { display: inline; margin-right: .4rem; }
  }
  .tch-pdf { display: inline-block; margin-left: .4rem; padding: .05rem .5rem; font-size: .75rem;
    border: 1px solid var(--global-theme-color); border-radius: 4px; vertical-align: middle; }
  .tch-pdf:hover { text-decoration: none; background: var(--global-theme-color); color: var(--global-bg-color) !important; }
  .tch-certs .tch-pdf i { font-size: .75rem; margin: 0; color: inherit; }
  .tch-certs .tch-now { display: inline-block; margin-left: .4rem; padding: .05rem .5rem; font-size: .7rem; font-weight: 600;
    letter-spacing: .04em; text-transform: uppercase; border-radius: 4px; vertical-align: middle;
    background: var(--global-theme-color); color: var(--global-bg-color); }
  .pdfm { display: none; position: fixed; inset: 0; z-index: 2000; background: rgba(10, 20, 25, .6);
    align-items: center; justify-content: center; padding: 2rem; }
  .pdfm.open { display: flex; }
  .pdfm-box { display: flex; flex-direction: column; width: min(900px, 100%); height: min(88vh, 1100px);
    background: var(--global-card-bg-color); border-radius: 10px; overflow: hidden;
    box-shadow: 0 12px 40px rgba(0, 0, 0, .35); }
  .pdfm-bar { display: flex; align-items: center; gap: 1rem; padding: .6rem .9rem;
    border-bottom: 1px solid var(--global-divider-color); }
  .pdfm-title { flex: 1; min-width: 0; font-weight: 600; font-size: .95rem; white-space: nowrap;
    overflow: hidden; text-overflow: ellipsis; color: var(--global-text-color); }
  .pdfm-open { font-size: .8rem; white-space: nowrap; }
  .pdfm-close { border: 0; background: none; font-size: 1.6rem; line-height: 1; padding: 0 .25rem;
    color: var(--global-text-color); cursor: pointer; }
  .pdfm-close:hover { color: var(--global-theme-color); }
  .pdfm iframe { flex: 1; width: 100%; border: 0; background: #fff; }
</style>

<div class="tch-section">Training &amp; Certifications</div>
<ul class="tch-certs">
  <li><i class="fa-solid fa-chalkboard-user"></i><div><a href="https://ctl.gatech.edu/fff/" target="_blank">Future Faculty Fellows Program</a> <span class="tch-now">In progress</span><span>Center for Teaching and Learning, Georgia Institute of Technology</span></div></li>
  <li><i class="fa-solid fa-award"></i><div>Teaching Preparation Series: Advanced Certification <a class="tch-pdf" href="/assets/pdf/teaching-preparation-series-certificate.pdf" target="_blank" data-pdf-modal="Teaching Preparation Series: Advanced Certificate"><i class="fa-solid fa-file-pdf"></i> Certificate</a><span>Center for Teaching &amp; Learning, The University of Texas at Austin</span></div></li>
  <li><i class="fa-solid fa-award"></i><div>Teaching Assistant Certification <a class="tch-pdf" href="/assets/pdf/Cockrell-certified-TA-certificate.pdf" target="_blank" data-pdf-modal="Cockrell Certified TA Certificate"><i class="fa-solid fa-file-pdf"></i> Certificate</a><span>Cockrell School of Engineering, The University of Texas at Austin</span></div></li>
</ul>

<div class="tch-section">Teaching</div>
<div class="tch-card">
  <div class="tch-when"><strong>2022 – 2023</strong>Aug. 2022 – Apr. 2023</div>
  <div class="tch-body">
    <h3 class="tch-role">Graduate Teaching Assistant</h3>
    <div class="tch-org"><i class="fa-solid fa-building-columns"></i>The University of Texas at Austin · Walker Department of Mechanical Engineering</div>
    <div class="tch-course">ME 139L · Experimental Heat Transfer Lab</div>
    <p>Led two lab sections per semester, teaching experimental design, uncertainty analysis, and the analysis of heat transfer systems.</p>
    <div class="tch-tags"><span>Experimental design</span><span>Uncertainty analysis</span><span>Systems analysis</span><span>Heat transfer</span></div>
  </div>
</div>

<div class="tch-section">Mentorship</div>
<div class="tch-card">
  <div class="tch-when"><strong>2022 – 2026</strong>Aug. 2022 – Aug. 2026</div>
  <div class="tch-body">
    <h3 class="tch-role">Research Mentor</h3>
    <div class="tch-org"><i class="fa-solid fa-flask"></i>Bahadur Research Group · The University of Texas at Austin</div>
    <p>Mentored and advised new members of the research group as they started their research projects.</p>
    <div class="tch-stats">
      <div class="tch-stat"><b>2</b><small>Ph.D. students</small></div>
      <div class="tch-stat"><b>1</b><small>Master's student</small></div>
      <div class="tch-stat"><b>2</b><small>Undergraduates</small></div>
    </div>
  </div>
</div>

<!-- Pop-up PDF viewer used by any link with data-pdf-modal="Title" -->
<div class="pdfm" id="pdf-modal" role="dialog" aria-modal="true" aria-labelledby="pdfm-title">
  <div class="pdfm-box">
    <div class="pdfm-bar">
      <span class="pdfm-title" id="pdfm-title"></span>
      <a class="pdfm-open" href="#" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i> Open in new tab</a>
      <button class="pdfm-close" type="button" aria-label="Close">&times;</button>
    </div>
    <iframe title="PDF viewer"></iframe>
  </div>
</div>
<script>
  (function () {
    var modal = document.getElementById("pdf-modal");
    if (!modal) return;
    var frame = modal.querySelector("iframe");
    var title = modal.querySelector(".pdfm-title");
    var openTab = modal.querySelector(".pdfm-open");
    var lastLink = null;
    function close() {
      modal.classList.remove("open");
      frame.removeAttribute("src");
      document.body.style.overflow = "";
      if (lastLink) lastLink.focus();
    }
    document.querySelectorAll("a[data-pdf-modal]").forEach(function (link) {
      link.addEventListener("click", function (e) {
        // Phones usually can't show a PDF inside a page, so let them open it normally.
        if (window.matchMedia("(max-width: 575.98px)").matches) return;
        e.preventDefault();
        lastLink = link;
        title.textContent = link.getAttribute("data-pdf-modal") || "Document";
        openTab.href = link.href;
        frame.src = link.href;
        modal.classList.add("open");
        document.body.style.overflow = "hidden";
        modal.querySelector(".pdfm-close").focus();
      });
    });
    modal.querySelector(".pdfm-close").addEventListener("click", close);
    modal.addEventListener("click", function (e) { if (e.target === modal) close(); });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && modal.classList.contains("open")) close();
    });
  })();
</script>
