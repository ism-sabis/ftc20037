---
layout: page
title: Awards
description: Our team's achievements and recognition over the years.
permalink: /awards/
---

<div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
  <!-- Header -->
  <section class="mb-12">
    <p class="text-sm font-semibold text-[var(--color-accent)] uppercase tracking-wide mb-2">Achievements</p>
    <h1 class="text-3xl md:text-4xl font-bold text-[var(--color-text)] mb-4">Awards & Recognition</h1>
    <p class="text-[var(--color-text-muted)]">Our team's accomplishments and the recognition we've received for our hard work in engineering, outreach, and teamwork.</p>
  </section>

  <!-- All Awards -->
  <section class="mb-16">
    {% assign sorted_awards = site.data.awards | sort: "season" | reverse %}
    {% assign current_season = "" %}

    {% for award in sorted_awards %}
    {% if award.season != current_season %}
    {% assign current_season = award.season %}
    <h2 class="text-xl font-semibold" style="color: var(--color-text)" mt-8 mb-4 pb-2 border-b border-[var(--color-border)]>{{ current_season }} Season</h2>
    {% endif %}

    <div class="bg-[var(--color-surface)] rounded-lg p-6 border border-[var(--color-border)] hover:border-[var(--color-accent)] transition-colors mb-4">
      <div class="flex items-start gap-4">
        <svg class="h-8 w-8 text-[var(--color-accent)] flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"/></svg>
        <div class="flex-1">
          <h3 class="font-semibold text-lg" style="color: var(--color-text)">{{ award.name }}</h3>
          <p class="text-sm font-medium" style="color: var(--color-accent)" mt-1>{{ award.event }}</p>
          {% if award.description %}
          <p class="text-sm text-[var(--color-text-muted)] mt-2">{{ award.description }}</p>
          {% endif %}
        </div>
      </div>
    </div>
    {% endfor %}
  </section>

  <!-- Award Criteria -->
  <section class="mb-16 bg-[var(--color-surface-elevated)] rounded-lg p-8 border border-[var(--color-border)]">
    <p class="text-sm font-semibold text-[var(--color-accent)] uppercase tracking-wide mb-2">About Awards</p>
    <h2 class="text-2xl font-bold" style="color: var(--color-text)" mb-6">FIRST Core Values Awards</h2>

    <div class="grid md:grid-cols-2 gap-4">
      <div class="bg-[var(--color-surface)] rounded-lg p-4 border border-[var(--color-border)] hover:border-[var(--color-accent)] transition-colors">
        <h3 class="font-semibold mb-1" style="color: var(--color-text)">Inspire Award</h3>
        <p class="text-sm text-[var(--color-text-muted)]">The highest honor, recognizing a team that best embodies the FIRST mission.</p>
      </div>

      <div class="bg-[var(--color-surface)] rounded-lg p-4 border border-[var(--color-border)] hover:border-[var(--color-accent)] transition-colors">
        <h3 class="font-semibold mb-1" style="color: var(--color-text)">Think Award</h3>
        <p class="text-sm text-[var(--color-text-muted)]">Excellence in engineering documentation and process.</p>
      </div>

      <div class="bg-[var(--color-surface)] rounded-lg p-4 border border-[var(--color-border)] hover:border-[var(--color-accent)] transition-colors">
        <h3 class="font-semibold mb-1" style="color: var(--color-text)">Connect Award</h3>
        <p class="text-sm text-[var(--color-text-muted)]">Outstanding outreach and community engagement.</p>
      </div>

      <div class="bg-[var(--color-surface)] rounded-lg p-4 border border-[var(--color-border)] hover:border-[var(--color-accent)] transition-colors">
        <h3 class="font-semibold mb-1" style="color: var(--color-text)">Innovate Award</h3>
        <p class="text-sm text-[var(--color-text-muted)]">Creative and effective robot design solutions.</p>
      </div>

      <div class="bg-[var(--color-surface)] rounded-lg p-4 border border-[var(--color-border)] hover:border-[var(--color-accent)] transition-colors">
        <h3 class="font-semibold mb-1" style="color: var(--color-text)">Control Award</h3>
        <p class="text-sm text-[var(--color-text-muted)]">Exceptional autonomous control.</p>
      </div>

      <div class="bg-[var(--color-surface)] rounded-lg p-4 border border-[var(--color-border)] hover:border-[var(--color-accent)] transition-colors">
        <h3 class="font-semibold mb-1" style="color: var(--color-text)">Motivate Award</h3>
        <p class="text-sm text-[var(--color-text-muted)]">Best team spirit and enthusiasm.</p>
      </div>

      <div class="bg-[var(--color-surface)] rounded-lg p-4 border border-[var(--color-border)] hover:border-[var(--color-accent)] transition-colors md:col-span-2 max-w-md">
        <h3 class="font-semibold mb-1" style="color: var(--color-text)">Design Award</h3>
        <p class="text-sm text-[var(--color-text-muted)]">Outstanding robot aesthetics and industrial design.</p>
      </div>
    </div>
  </section>

  <!-- CTA -->
  <section class="text-center bg-[var(--color-surface-elevated)] rounded-lg p-8 border border-[var(--color-border)] hover:border-[var(--color-accent)] transition-colors">
    <h2 class="text-2xl font-bold text-[var(--color-text)] mb-4">Want to help us earn more awards?</h2>
    <a href="{{ '/about/' | relative_url }}#join" class="inline-flex items-center px-6 py-2.5 bg-[var(--color-accent)] hover:bg-[var(--color-accent-dark)] text-white font-medium rounded-sm transition-colors focus-visible:ring-2 focus-visible:ring-[var(--color-accent)]">
      Join Our Team
    </a>
  </section>
</div>
