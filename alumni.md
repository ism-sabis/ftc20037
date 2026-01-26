---
layout: page
title: Alumni
description: Celebrating our graduated team members and their continued success.
permalink: /alumni/
---

Our alumni are a testament to the impact of FIRST robotics. These former team members have gone on to pursue careers and studies in engineering, science, business, and beyond.

## Where Are They Now?

<div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6 my-8">
{% for alum in site.data.alumni %}
<div class="card">
  <div class="aspect-square overflow-hidden">
    <img
      src="{{ alum.image | default: '/assets/images/placeholder.svg' | relative_url }}"
      alt="{{ alum.name }}"
      class="w-full h-full object-cover"
      loading="lazy"
    >
  </div>
  <div class="card-body">
    <h3 class="card-title">{{ alum.name }}</h3>
    <p class="text-primary font-medium">{{ alum.role }}</p>
    <p class="text-sm text-[var(--color-text-muted)]">Class of {{ alum.graduation_year }}</p>

    {% if alum.now %}
    <p class="mt-2 text-[var(--color-text-muted)]">
      <strong>Now:</strong> {{ alum.now }}
    </p>
    {% endif %}

    {% if alum.seasons %}
    <div class="flex flex-wrap gap-1 mt-2">
      {% for season in alum.seasons %}
      <span class="badge bg-[var(--color-surface)] text-xs">{{ season }}</span>
      {% endfor %}
    </div>
    {% endif %}
  </div>
</div>
{% endfor %}
</div>

{% if site.data.alumni.size == 0 %}
<div class="card">
  <div class="card-body text-center py-12">
    <p class="text-[var(--color-text-muted)]">Alumni listing coming soon!</p>
  </div>
</div>
{% endif %}

---

## Stay Connected

Alumni, we'd love to hear from you! If you'd like to:
- Share your career updates
- Mentor current team members
- Speak at team events
- Contribute to our alumni network

Please [contact us](/contact/)!
