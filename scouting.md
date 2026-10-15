---
layout: default
title: BIOBUZZ Scouting
description: Share your FTC team's BIOBUZZ robot capabilities and typical tournament-day performance.
permalink: /scouting/
extra_css: /assets/css/scouting.css
extra_js: /assets/js/scouting.js
---

<div class="scouting-page">
  <section class="scouting-hero" aria-labelledby="scouting-title">
    <div class="scouting-hero__inner">
      <div class="scouting-hero__copy">
        <p class="scouting-eyebrow">FTC {{ site.site.team_number }} <span aria-hidden="true">/</span> {{ site.site.current_season }} season</p>
        <h1 id="scouting-title">Make your robot easy to scout.</h1>
        <p class="scouting-hero__lead">Share what your robot can do and how it is performing at this tournament. Profiles are for alliance scouting.</p>
        <a class="scouting-hero__link" href="#team-profile">Go to the team profile <span aria-hidden="true">↓</span></a>
      </div>

      <aside class="scouting-clock" aria-label="BIOBUZZ match timing">
        <p class="scouting-clock__heading">Match clock</p>
        <ol class="scouting-clock__list">
          <li><span class="scouting-clock__time">0:30</span><span><strong>AUTO</strong><small>Robot runs on its own</small></span></li>
          <li><span class="scouting-clock__time">0:08</span><span><strong>TRANSITION</strong><small>Between match periods</small></span></li>
          <li><span class="scouting-clock__time">2:00</span><span><strong>TELEOP</strong><small>Drivers take control</small></span></li>
          <li class="scouting-clock__unlock"><span class="scouting-clock__time">1:00</span><span><strong>FLOWERS OPEN</strong><small>At one minute remaining</small></span></li>
        </ol>
      </aside>
    </div>
  </section>

  <div class="scouting-content">
    <div class="scouting-preview" role="status">
      <span class="scouting-preview__tag">Preview only</span>
      <p><strong>Submissions are not open yet.</strong> You can explore the fields, but nothing you enter is sent or saved.</p>
    </div>

    <section id="team-profile" class="scouting-profile" aria-labelledby="team-profile-title">
      <header class="scouting-profile__header">
        <div>
          <p class="scouting-section-kicker">Tournament-day profile</p>
          <h2 id="team-profile-title">Your BIOBUZZ robot</h2>
          <p>Report current capabilities and typical results for this tournament day. Use your robot’s contribution, not the alliance’s total score.</p>
        </div>
        <span class="scouting-profile__stamp" aria-hidden="true">FTC<br>{{ site.site.team_number }}</span>
      </header>

      <fieldset class="scouting-event">
        <legend>Event and team</legend>
        <div class="scouting-event__grid">
          <div class="scouting-control">
            <label for="scouting-tournament">Tournament <span class="scouting-required">Required</span></label>
            <select id="scouting-tournament" class="scouting-input" required aria-required="true">
              <option value="">Choose a tournament</option>
            </select>
          </div>
          <div class="scouting-control">
            <label for="scouting-day">Competition day <span class="scouting-required">Required</span></label>
            <select id="scouting-day" class="scouting-input" required aria-required="true" disabled>
              <option value="">Choose a day</option>
            </select>
          </div>
        </div>
        <p class="scouting-event__hint">Each profile is tied to one tournament and day. When submissions are enabled, updates will replace that team’s previous profile after confirmation.</p>
      </fieldset>

      <div id="scouting-questions" class="scouting-questions" aria-live="polite">
        <p class="scouting-loading">Loading profile questions…</p>
      </div>

      <div class="scouting-save">
        <button class="scouting-save__button" type="button" disabled>Submissions not open yet</button>
        <p>Do not enter personal or contact information. This preview does not collect responses.</p>
      </div>
    </section>

    <section class="scouting-robot" aria-labelledby="our-robot-title">
      <div class="scouting-robot__header">
        <div>
          <p class="scouting-section-kicker">{{ site.site.team_name }} · FTC {{ site.site.team_number }}</p>
          <h2 id="our-robot-title">Our robot and capabilities</h2>
        </div>
      </div>
      <div id="our-robot-summary" class="scouting-robot__slot"></div>
    </section>

    <script id="scouting-question-config" type="application/json">{{ site.data.scouting | jsonify }}</script>
    {% assign competition_events = site.data.events | where: "type", "competition" %}
    <script id="scouting-event-config" type="application/json">{{ competition_events | jsonify }}</script>
    <noscript>
      <p class="scouting-noscript">JavaScript is required to display the profile questions. Submissions are not being collected.</p>
    </noscript>
  </div>
</div>
