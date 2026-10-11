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

## Current Season

The 2026-2027 FTC game is **BIOBUZZ presented by RTX**, part of FIRST CANOPY. Our robot does not have a name yet. The current season page lists our two announced Sunday qualifiers in New Brighton and Elk River, Minnesota.

- **Team:** Six current students, with one additional member profile coming soon
- **Events:** New Brighton Qualifier and Elk River Qualifier, both on Sundays

[View current season details →](/season/)

---

## Engineering Process

### Design Philosophy
Our design method is iterative and evidence-based:

Identify -> Ideate -> Design -> Create -> Test

This process is inherited from former team Catlateral Damage and applied to both hardware and software.

### Documentation
- Engineering notebook maintained throughout the season
- CAD models created in Onshape
- Regular design reviews with mentors

---

## Awards History

{% for award in site.data.awards limit: 6 %}
- **{{ award.name }}** - {{ award.event }} ({{ award.season }})
{% endfor %}

[View all awards →](/awards/)

---

## Outreach Impact

Our outreach strategy has two themes: Motivate and Connect.

- **Valentine's Bot Event:** Campus robot gift-delivery activity that engaged hundreds of students
- **International Day Exhibition:** Robotics room with demos, notebook walkthroughs, and STEM activities
- **City Park Demo:** Public drive experience and FTC systems education
- **Industry Collaboration:** Esmeril Industries tour and custom coupler support for lift torque issue

---

## Team Culture

### Core Values
- **Gracious Professionalism:** We compete hard but treat everyone with respect
- **Coopertition:** We help other teams succeed
- **Continuous Learning:** We embrace challenges as opportunities to grow

### Sustainability
- 3D printing and laser cutting reduce fabrication costs
- Annual recruitment ensures continuity and role handoff

### Team and Mentor Snapshot

- Team members: {% for member in site.data.team %}{{ member.name }}{% unless forloop.last %}, {% endunless %}{% endfor %}
- Additional member profile: Coming soon
- Mentor: Erik (Lead Mentor, engineer at Amazon)

---

## Quick Links

- [Current Season Details](/season/)
- [About Our Team](/about/)

---

<div class="text-center text-sm text-[var(--color-text-muted)] mt-8">
  <p>{{ site.site.team_name }} | Team #{{ site.site.team_number }}</p>
  <p>{{ site.site.current_season }} Season</p>
</div>
