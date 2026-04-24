---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

<style>
.cv-card {
  padding: 1.4rem 1.6rem;
  margin: 1.2rem 0;
  border-radius: 18px;
  border: 1px solid rgba(120,120,120,0.18);
  background: var(--global-bg-color, #ffffff);
  box-shadow: 0 6px 18px rgba(0,0,0,0.06);
}

.cv-header {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.cv-logo-box {
  flex: 0 0 110px;
  aspect-ratio: 3 / 1;
  background: #ffffff;
  border-radius: 10px;
  border: 1px solid rgba(120,120,120,0.15);
  padding: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.cv-logo-box img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.cv-header-text {
  flex: 1;
  min-width: 0;
}

.cv-title {
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--global-text-color, #222);
  line-height: 1.3;
}

.cv-subtitle {
  font-size: 0.95rem;
  color: #2c6e91;
  margin-top: 3px;
  line-height: 1.35;
}

.cv-meta {
  font-size: 0.85rem;
  color: var(--global-text-color-light, #777);
  margin-top: 3px;
  line-height: 1.35;
}

.cv-divider {
  margin: 0.9rem 0 0.75rem 0;
  height: 1px;
  background: rgba(120,120,120,0.15);
}

.cv-content {
  padding-left: 126px;
}

.cv-desc {
  font-size: 0.92rem;
  line-height: 1.65;
  color: var(--global-text-color, #333);
  margin: 0;
}

.cv-list {
  margin: 0;
  padding-left: 1.1rem;
  font-size: 0.92rem;
  line-height: 1.6;
  color: var(--global-text-color, #333);
}

.cv-list li {
  margin-bottom: 6px;
}

.cv-grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  align-items: stretch;
}

.cv-grid-3 .cv-card {
  margin: 0;
  height: 100%;
}

.cv-simple-card {
  padding-left: 1.4rem;
}

@media (max-width: 900px) {
  .cv-grid-3 {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 700px) {
  .cv-card {
    padding: 1.2rem;
  }

  .cv-header {
    flex-direction: column;
    align-items: flex-start;
  }

  .cv-logo-box {
    width: 140px;
    flex: none;
  }

  .cv-content {
    padding-left: 0;
  }
}

/* Dark mode */
html[data-theme="dark"] .cv-card {
  background: #1e1e1e;
  border: 1px solid rgba(255,255,255,0.08);
  box-shadow: 0 6px 18px rgba(0,0,0,0.35);
}

html[data-theme="dark"] .cv-title {
  color: #f1f1f1;
}

html[data-theme="dark"] .cv-subtitle {
  color: #5fa8d3;
}

html[data-theme="dark"] .cv-meta {
  color: #aaaaaa;
}

html[data-theme="dark"] .cv-divider {
  background: rgba(255,255,255,0.10);
}

html[data-theme="dark"] .cv-desc,
html[data-theme="dark"] .cv-list {
  color: #e2e2e2;
}
</style>

## Work Experience

<div class="cv-card">
  <div class="cv-header">
    <div class="cv-logo-box">
      <img src="/images/School_Mar_Geo_logoISMAR.jpg" alt="CNR ISMAR logo">
    </div>

    <div class="cv-header-text">
      <div class="cv-title">Postdoctoral Researcher</div>
      <div class="cv-subtitle">CNR – Institute of Marine Sciences (ISMAR), Rome, Italy</div>
      <div class="cv-meta">Dec 2024 – Present · Supervisor: <a href="https://www.researchgate.net/profile/Emanuele-Organelli">Dr. Emanuele Organelli</a></div>
    </div>
  </div>

  <div class="cv-divider"></div>

  <div class="cv-content">
    <ul class="cv-list">
      <li>Investigation of ocean carbon cycling processes, including biological and microbial carbon pumps, by combining BGC-Argo observations, ocean colour satellite observations, and reconstruction outputs.</li>
      <li>Implemented a MATLAB-based processing pipeline for BGC-Argo data, integrating data processing, quality control (QC), and analysis workflows.</li>
      <li>Bio-optical and biogeochemical data processing and dataset establishment from BGC-Argo profiles.</li>
    </ul>
  </div>
</div>

## Education

<div class="cv-card">
  <div class="cv-header">
    <div class="cv-logo-box">
      <img src="/images/ecnu.png" alt="East China Normal University logo">
    </div>

    <div class="cv-header-text">
      <div class="cv-title">Doctor of Science in Physical Oceanography</div>
      <div class="cv-subtitle">East China Normal University, State Key Laboratory of Estuarine and Coastal Research (SKLEC), Shanghai, China</div>
      <div class="cv-meta">Sep 2018 – Jun 2024 · GPA: 3.46/4 · Supervisor: <a href="https://www.researchgate.net/profile/Fang-Shen-6">Prof. Fang Shen</a></div>
    </div>
  </div>

  <div class="cv-divider"></div>

  <div class="cv-content">
    <p class="cv-desc">
      I explored the inherent optical properties of marine particle compositions. I designed and conducted laboratory experiments to quantify the refractive indices of mineral particles, detritus, and different phytoplankton groups. I then investigated the contributions of phytoplankton and organic detritus to particulate organic carbon in optically complex estuarine, coastal, and shelf seas of China. I also analysed changes in particle types under atmospheric deposition and the associated phytoplankton responses. I developed MATLAB-based workflows for analysing satellite and float datasets, and implemented C++ simulations of particle backscattering processes. During this period, I also served as the administrator of the optical and phytoplankton laboratory.
    </p>
  </div>
</div>

<div class="cv-card">
  <div class="cv-header">
    <div class="cv-logo-box">
      <img src="/images/School_Mar_Geo_logoISMAR.jpg" alt="CNR ISMAR logo">
    </div>

    <div class="cv-header-text">
      <div class="cv-title">Visiting PhD (China Scholarship Council)</div>
      <div class="cv-subtitle">CNR – Institute of Marine Sciences (ISMAR), Rome, Italy</div>
      <div class="cv-meta">Oct 2022 – Oct 2023 · Co-supervisor: <a href="https://www.researchgate.net/profile/Emanuele-Organelli">Dr. Emanuele Organelli</a></div>
    </div>
  </div>

  <div class="cv-divider"></div>

  <div class="cv-content">
    <p class="cv-desc">
      The primary focus was on analysing the inherent optical properties of particles and conducting scattering simulations in the estuarine, coastal, and shelf seas of China. In addition, based on BGC-Argo data, I analysed the ecological impact of marine heatwaves on the upper waters of the north-western Mediterranean Sea within the CAREHeat Project.
    </p>
  </div>
</div>

<div class="cv-card">
  <div class="cv-header">
    <div class="cv-logo-box">
      <img src="/images/OUC.png" alt="Ocean University of China logo">
    </div>

    <div class="cv-header-text">
      <div class="cv-title">Bachelor of Science in Marine Technology</div>
      <div class="cv-subtitle">Ocean University of China, College of Information Science and Engineering, Qingdao, China</div>
      <div class="cv-meta">Sep 2014 – Jun 2018 · GPA: 3.55/4 · Supervisors: 
        <a href="https://www.researchgate.net/profile/Shuguo-Chen">Prof. Shuguo Chen</a> and 
        <a href="https://www.researchgate.net/profile/Chen-Ge-5">Prof. Ge Chen</a>
      </div>
    </div>
  </div>

  <div class="cv-divider"></div>

  <div class="cv-content">
    <p class="cv-desc">
      My work utilized multi-source remote sensing data to investigate the causal and time-lag relationships between East Asian dust storm deposition and phytoplankton biomass in the East China Sea. I developed programming skills in C, C++, Python, MATLAB, R, and Assembly, and ultimately applied MATLAB as the primary tool for data analysis and implementation of this study.
    </p>
  </div>
</div>

## Awards

<div class="cv-card cv-simple-card">
  <ul class="cv-list">
    <li>China Scholarship Council (CSC) Scholarship, Grant No. 202206140082, €16,200 per year, 2022 to 2023</li>
    <li>Outstanding Student Award, East China Normal University, 2021 to 2022</li>
    <li>Outstanding Undergraduate Dissertation Award, Ocean University of China, 2018</li>
    <li>Outstanding Student Award, Ocean University of China, 2016 to 2017</li>
    <li>Scholarship for Excellence in Academic Work, Ocean University of China, 2014 to 2017</li>
    <li>Scholarship for Participation in Social Activities, Ocean University of China, 2016 to 2017</li>
  </ul>
</div>

## Skills

<div class="cv-grid-3">

<div class="cv-card">
  <div class="cv-title">Languages</div>
  <div class="cv-divider"></div>
  <ul class="cv-list">
    <li>Chinese, Mandarin <small>native</small></li>
    <li>English <small>proficient</small></li>
    <li>Italian <small>conversational</small></li>
    <li>Japanese <small>conversational</small></li>
  </ul>
</div>

<div class="cv-card">
  <div class="cv-title">Programming</div>
  <div class="cv-divider"></div>
  <ul class="cv-list">
    <li>MATLAB <small>advanced</small></li>
    <li>Python / R <small>intermediate</small></li>
    <li>C / C++ / Assembly <small>basic</small></li>
    <li>ENVI, SNAP, SeaDAS</li>
    <li>Adobe Photoshop, Microsoft Office</li>
  </ul>
</div>

<div class="cv-card">
  <div class="cv-title">Scientific Instruments / Measurements</div>
  <div class="cv-divider"></div>
  <ul class="cv-list">
    <li>LISST-200X, Sequoia Scientific</li>
    <li>HyperSAS, Sea-Bird Scientific</li>
    <li>AC-S / ECO-BB9 / ECO-VSF, WET Labs</li>
    <li>Spectrophotometer, PerkinElmer</li>
    <li>Mastersizer, Malvern</li>
  </ul>
</div>

</div>

## Certifications

<div class="cv-card">
  <div class="cv-title">STCW Certifications</div>
  <div class="cv-subtitle">Tecno Italian Safety and Survival Training S.r.l, Italy</div>
  <div class="cv-meta">Issued: Mar 2025</div>

  <div class="cv-divider"></div>

  <ul class="cv-list">
    <li>Personal Survival Techniques</li>
    <li>Fire Prevention and Fire Fighting</li>
    <li>Elementary First Aid</li>
    <li>Personal Safety and Social Responsibilities</li>
  </ul>
</div>
