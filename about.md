---
layout: page
title: About Us
description: Learn about our team's history, mission, and the passionate students who make it all happen.
permalink: /about/
---

<div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
  <!-- Mission -->
  <section class="mb-16">
    <p class="text-sm font-semibold text-[var(--color-accent)] uppercase tracking-wide mb-2">Our Mission</p>
    <h2 class="text-3xl md:text-4xl font-bold text-[var(--color-text)] mb-6">About Standard Deviation</h2>
    <div class="prose prose-lg max-w-none">
      <p>We are a FIRST {{ site.site.program }} team dedicated to improving ourselves and our community through outreach, STEM learning, and inspiring younger students to explore robotics and engineering.</p>
      <p>We also uphold <strong>Gracious Professionalism</strong> and <strong>Coopertition</strong> as the core values behind how we compete and collaborate.</p>
    </div>
  </section>

  <!-- Team History -->
  {% assign history = site.data.team_history %}
  {% if history %}
  <section class="mb-16">
    <p class="text-sm font-semibold text-[var(--color-accent)] dark:text-[var(--color-accent-light)] uppercase tracking-wider mb-2">History</p>
    <h2 class="text-3xl md:text-4xl font-bold text-[var(--color-text)] mb-8">Our Journey</h2>
    {% include components/timeline.html events=history %}
  </section>
  {% else %}
  <section class="mb-16">
    <p class="text-sm font-semibold text-[var(--color-accent)] dark:text-[var(--color-accent-light)] uppercase tracking-wider mb-2">History</p>
    <h2 class="text-3xl md:text-4xl font-bold text-[var(--color-text)] mb-8">Our Journey</h2>
    <div class="prose prose-lg max-w-none" style="color: var(--color-text-muted)">
      <p>Our team was founded with a simple goal: give students the opportunity to learn real-world engineering skills while having fun competing in robotics competitions.</p>
      <p>Since our founding, we've grown from a small group of students meeting after school to a thriving program with multiple subteams, dedicated mentors, and a track record of success at competitions.</p>
    </div>
  </section>
  {% endif %}

  <!-- Team -->
  <section class="mb-16">
    <p class="text-sm font-semibold text-[var(--color-accent)] dark:text-[var(--color-accent-light)] uppercase tracking-wider mb-2">People</p>
    <h2 class="text-3xl md:text-4xl font-bold text-[var(--color-text)] mb-4">Our Team</h2>
    <div class="w-12 h-0.5 bg-[var(--color-accent)] mb-6"></div>
    <p class="text-[var(--color-text-muted)] mb-8">Standard Deviation is a team of students from the International School of Minnesota in Eden Prairie, Minnesota.</p>

    <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6 my-8">
      {% for member in site.data.team %}
      {% include components/team-member-card.html member=member %}
      {% endfor %}
    </div>

    <h3 class="text-xl font-semibold text-[var(--color-text)] mt-12 mb-4">Mentors</h3>
    <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6 my-8">
      {% for mentor in site.data.mentors %}
      {% include components/team-member-card.html member=mentor %}
      {% endfor %}
    </div>
  </section>

  <!-- What We Do -->
  <section class="mb-16">
    <p class="text-sm font-semibold text-[var(--color-accent)] dark:text-[var(--color-accent-light)] uppercase tracking-wider mb-2">Activities</p>
    <h2 class="text-3xl md:text-4xl font-bold text-[var(--color-text)] mb-8">What We Do</h2>

    <div class="grid md:grid-cols-3 gap-6">
      <div class="bg-[var(--color-surface-elevated)] dark:bg-[var(--color-surface)] rounded-sm p-6 border border-[var(--color-border)] dark:border-[var(--color-border-strong)] hover:border-[var(--color-accent)] transition-colors">
        <h3 class="text-lg font-semibold text-[var(--color-text)] mb-2">Build Season</h3>
        <p class="text-sm text-[var(--color-text-muted)]">During build season, we design, build, and program a competition robot in just a few weeks. This intense period teaches us project management, teamwork, and problem-solving.</p>
      </div>

      <div class="bg-[var(--color-surface-elevated)] dark:bg-[var(--color-surface)] rounded-sm p-6 border border-[var(--color-border)] dark:border-[var(--color-border-strong)] hover:border-[var(--color-accent)] transition-colors">
        <h3 class="text-lg font-semibold text-[var(--color-text)] mb-2">Competition Season</h3>
        <p class="text-sm text-[var(--color-text-muted)]">We compete at local league meets, qualifiers, and championships. These events are not just about winning - they're about learning, collaborating with other teams, and having fun.</p>
      </div>

      <div class="bg-[var(--color-surface-elevated)] dark:bg-[var(--color-surface)] rounded-sm p-6 border border-[var(--color-border)] dark:border-[var(--color-border-strong)] hover:border-[var(--color-accent)] transition-colors">
        <h3 class="text-lg font-semibold text-[var(--color-text)] mb-2">Outreach</h3>
        <p class="text-sm text-[var(--color-text-muted)]">We're committed to giving back to our community. We host STEM workshops, mentor younger teams, and demonstrate robotics at local events to inspire the next generation of engineers.</p>
      </div>
    </div>
  </section>

  <!-- Portfolio -->
  <section class="mb-16">
    <p class="text-sm font-semibold text-[var(--color-accent)] uppercase tracking-wide mb-2">Engineering</p>
    <h2 class="text-3xl md:text-4xl font-bold text-[var(--color-text)] mb-4">Our Portfolio</h2>
    <p class="text-[var(--color-text-muted)] mb-6">Our engineering portfolio showcases the full story of Team Standard Deviation — from our design process and robot build to community outreach.</p>

    <div class="bg-[var(--color-surface)] rounded-lg p-6 border border-[var(--color-border)] hover:border-[var(--color-accent)] transition-colors">
      <div class="flex flex-col sm:flex-row items-center gap-4">
        <svg class="h-12 w-12 text-[var(--color-accent)]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
        <div class="flex-1">
          <h3 class="font-semibold text-lg mb-1 text-[var(--color-text)]">2025-2026 Robotics Portfolio</h3>
          <p class="text-sm text-[var(--color-text-muted)] mb-4">Explore our comprehensive engineering notebook covering robot design and outreach efforts.</p>
          <div class="flex flex-col sm:flex-row gap-3">
            <a href="{{ '/portfolio/' | relative_url }}" class="inline-flex items-center justify-center px-5 py-2.5 bg-[var(--color-accent)] hover:bg-[var(--color-accent-dark)] text-white font-medium rounded-sm transition-colors focus-visible:ring-2 focus-visible:ring-[var(--color-accent)]">View Portfolio</a>
            <a href="{{ '/assets/images/Robotics Portfolio 2025-2026.pdf?v=' | relative_url }}{{ site.time | date: '%s' }}" download class="inline-flex items-center justify-center px-5 py-2.5 border-2 border-[var(--color-primary)] text-[var(--color-primary)] hover:bg-[var(--color-primary)] hover:text-white font-medium rounded-sm transition-colors focus-visible:ring-2 focus-visible:ring-[var(--color-accent)]">Download PDF</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Join -->
<section id="join" class="mb-16 bg-[var(--color-surface-elevated)] rounded-lg p-8 border border-[var(--color-border)]">
    <p class="text-sm font-semibold text-[var(--color-accent)] uppercase tracking-wide mb-2">Get Involved</p>
    <h2 class="text-3xl md:text-4xl font-bold text-[var(--color-text)] mb-4">Join Our Team</h2>
    <p class="text-[var(--color-text-muted)] mb-6">We welcome students of all skill levels! Whether you're interested in building, design, marketing, or outreach - there's a place for you.</p>

    <div class="space-y-2 text-sm" style="color: var(--color-text-muted)" mb-6>
      <p><strong style="color: var(--color-text)">Requirements:</strong></p>
      <ul class="list-disc pl-5 space-y-1">
        <li>Be a student in grades 7-12</li>
        <li>Commit to attending team meetings regularly</li>
        <li>Have a passion for learning and teamwork</li>
      </ul>
    </div>

    <p class="text-sm font-semibold" style="color: var(--color-text)" mb-4>No prior experience necessary! We'll teach you everything you need to know.</p>

    <a href="{{ '/contact/' | relative_url }}" class="inline-flex items-center px-6 py-2.5 bg-[var(--color-accent)] hover:bg-[var(--color-accent-dark)] text-white font-medium rounded-sm transition-colors focus-visible:ring-2 focus-visible:ring-[var(--color-accent)]">
      Contact Us
    </a>
  </section>
</div>
