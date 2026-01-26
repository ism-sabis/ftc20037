---
layout: page
title: Awards
description: Our team's achievements and recognition over the years.
permalink: /awards/
---

We're proud of our team's accomplishments and the recognition we've received for our hard work in engineering, outreach, and teamwork.

## All Awards

<div class="space-y-4 my-8">
{% assign sorted_awards = site.data.awards | sort: "season" | reverse %}
{% assign current_season = "" %}

{% for award in sorted_awards %}
{% if award.season != current_season %}
{% assign current_season = award.season %}
<h3 class="text-xl font-bold mt-8 mb-4 border-b border-[var(--color-border)] pb-2">{{ current_season }} Season</h3>
{% endif %}

<div class="card">
  <div class="card-body flex items-start gap-4">
    <div class="text-4xl">🏆</div>
    <div>
      <h4 class="font-bold text-lg">{{ award.name }}</h4>
      <p class="text-primary">{{ award.event }}</p>
      {% if award.description %}
      <p class="text-[var(--color-text-muted)] mt-2">{{ award.description }}</p>
      {% endif %}
    </div>
  </div>
</div>
{% endfor %}
</div>

## Award Criteria

### FIRST Core Values Awards

- **Inspire Award** - The highest honor, recognizing a team that best embodies the FIRST mission
- **Think Award** - Excellence in engineering documentation and process
- **Connect Award** - Outstanding outreach and community engagement
- **Innovate Award** - Creative and effective robot design solutions
- **Control Award** - Exceptional autonomous programming
- **Motivate Award** - Best team spirit and enthusiasm
- **Design Award** - Outstanding robot aesthetics and industrial design

---

Want to help us earn more awards? [Join our team](/about/#join) or [become a sponsor](/sponsors/)!
