---
layout: page
title: Judge Mode
description: Quick reference for competition judges - key team information at a glance.
permalink: /judge/
---

<div class="no-print mb-8 p-4 bg-accent/10 rounded-lg">
  <p class="text-sm"><strong>Note:</strong> This page is optimized for competition judges. <a href="javascript:window.print()" class="text-primary">Print this page</a> for a portable reference.</p>
</div>

## Team Overview

<div class="grid md:grid-cols-3 gap-4 my-6">
  <div class="card">
    <div class="card-body text-center">
      <p class="text-4xl font-bold text-primary">{{ site.site.team_number }}</p>
      <p class="text-[var(--color-text-muted)]">Team Number</p>
    </div>
  </div>
  <div class="card">
    <div class="card-body text-center">
      <p class="text-4xl font-bold text-primary">{{ site.site.program }}</p>
      <p class="text-[var(--color-text-muted)]">Program</p>
    </div>
  </div>
  <div class="card">
    <div class="card-body text-center">
      <p class="text-4xl font-bold text-primary">{{ site.data.team.size }}</p>
      <p class="text-[var(--color-text-muted)]">Team Members</p>
    </div>
  </div>
</div>

---

## Robot Overview

Our robot for the {{ site.site.current_season }} season features:

- **Drivetrain:** [Describe drivetrain type]
- **Intake System:** [Describe intake mechanism]
- **Scoring Mechanism:** [Describe scoring system]
- **Autonomous Capability:** [Describe auto features]

[View detailed robot documentation →](/season/)

---

## Engineering Process

### Design Philosophy
Our team follows an iterative design process, using CAD modeling, prototyping, and testing to refine our robot design throughout the season.

### Documentation
- Engineering notebook maintained throughout the season
- CAD models created in [Software Name]
- Code version controlled on GitHub
- Regular design reviews with mentors

[View our documentation →](/docs/)

---

## Awards History

{% for award in site.data.awards limit: 6 %}
- **{{ award.name }}** - {{ award.event }} ({{ award.season }})
{% endfor %}

[View all awards →](/awards/)

---

## Outreach Impact

Our team is committed to giving back to our community through STEM outreach:

- **STEM Workshops:** Regular workshops at local schools
- **Team Mentorship:** Supporting newer FTC/FRC teams
- **Community Events:** Demonstrations at local events
- **Social Media:** Sharing our journey online

---

## Team Culture

### Core Values
- **Gracious Professionalism:** We compete hard but treat everyone with respect
- **Coopertition:** We help other teams succeed
- **Continuous Learning:** We embrace challenges as opportunities to grow

### Sustainability
- Mentor training program ensures knowledge transfer
- Comprehensive documentation for future seasons
- Alumni involvement and support

---

## Quick Links

- [Current Season Details](/season/)
- [Team Documentation](/docs/)
- [About Our Team](/about/)
- [Our Sponsors](/sponsors/)

---

<div class="text-center text-sm text-[var(--color-text-muted)] mt-8">
  <p>{{ site.site.team_name }} | Team #{{ site.site.team_number }}</p>
  <p>{{ site.site.current_season }} Season</p>
</div>
