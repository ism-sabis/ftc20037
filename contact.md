---
layout: page
title: Contact Us
description: Get in touch with Team Standard Deviation for questions, collaboration, or joining information.
permalink: /contact/
---

<div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
  <!-- Header -->
  <section class="mb-12">
    <p class="text-sm font-semibold text-red-600 dark:text-red-400 uppercase tracking-wider mb-2">Reach Out</p>
    <h1 class="text-3xl md:text-4xl font-bold text-gray-900 dark:text-white mb-4">Contact Us</h1>
    <p class="text-gray-600 dark:text-gray-400">We'd love to hear from you. If you are interested in joining the team, collaborating on outreach, or learning more about our season, please reach out.</p>
  </section>

  <!-- Contact Cards -->
  <section class="mb-12">
    <div class="grid md:grid-cols-2 gap-6">
      <div class="bg-white dark:bg-gray-900 rounded-xl p-6 border border-gray-100 dark:border-gray-700">
        <svg class="h-8 w-8 text-red-500 mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
        <h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-2">General Inquiries</h3>
        <p class="text-sm text-gray-600 dark:text-gray-400 mb-4">Questions about our team, joining, or general information.</p>
        {% if site.socials.email %}
        <a href="mailto:{{ site.socials.email }}" class="inline-flex items-center gap-2 px-5 py-2.5 bg-red-600 hover:bg-red-700 text-white font-medium rounded-lg transition-colors focus-visible:ring-2 focus-visible:ring-red-500 focus-visible:outline-none">
          <svg class="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
          Email Us
        </a>
        {% else %}
        <p class="text-sm text-gray-600 dark:text-gray-400"><em>Contact form coming soon.</em></p>
        {% endif %}
      </div>

      <div class="bg-white dark:bg-gray-900 rounded-xl p-6 border border-gray-100 dark:border-gray-700">
        <svg class="h-8 w-8 text-red-500 mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/></svg>
        <h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-2">Team Details</h3>
        <div class="space-y-2 text-sm text-gray-600 dark:text-gray-400">
          <p><strong class="text-gray-900 dark:text-white">Team:</strong> {{ site.site.team_name }} ({{ site.site.program }} #{{ site.site.team_number }})</p>
          <p><strong class="text-gray-900 dark:text-white">School:</strong> International School of Minnesota</p>
          <p><strong class="text-gray-900 dark:text-white">Location:</strong> Eden Prairie, Minnesota</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Follow Us -->
  <section class="mb-12 bg-gray-50 dark:bg-gray-800 rounded-xl p-8 border border-gray-100 dark:border-gray-700">
    <p class="text-sm font-semibold text-red-600 dark:text-red-400 uppercase tracking-wider mb-2">Social</p>
    <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-4">Follow Us</h2>
    <p class="text-gray-600 dark:text-gray-400 mb-6">Stay connected and follow our journey through the season!</p>

    <div class="flex flex-wrap gap-3">
      {% if site.socials.instagram and site.socials.instagram != "" %}
      <a href="{{ site.socials.instagram }}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 px-5 py-2.5 border border-gray-300 dark:border-gray-600 text-gray-700 dark:text-gray-300 hover:bg-white dark:hover:bg-gray-900 font-medium rounded-lg transition-colors focus-visible:ring-2 focus-visible:ring-red-500 focus-visible:outline-none">
        <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073z"/></svg>
        Instagram
      </a>
      {% endif %}

      {% if site.socials.github and site.socials.github != "" %}
      <a href="{{ site.socials.github }}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 px-5 py-2.5 border border-gray-300 dark:border-gray-600 text-gray-700 dark:text-gray-300 hover:bg-white dark:hover:bg-gray-900 font-medium rounded-lg transition-colors focus-visible:ring-2 focus-visible:ring-red-500 focus-visible:outline-none">
        <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
        GitHub
      </a>
      {% endif %}

      {% if site.socials.youtube and site.socials.youtube != "" %}
      <a href="{{ site.socials.youtube }}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 px-5 py-2.5 border border-gray-300 dark:border-gray-600 text-gray-700 dark:text-gray-300 hover:bg-white dark:hover:bg-gray-900 font-medium rounded-lg transition-colors focus-visible:ring-2 focus-visible:ring-red-500 focus-visible:outline-none">
        <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
        YouTube
      </a>
      {% endif %}
    </div>
  </section>

  <!-- Visit Us -->
  <section class="mb-12">
    <h2 class="text-xl font-semibold text-gray-900 dark:text-white mb-3">Visit Us</h2>
    <p class="text-gray-600 dark:text-gray-400">We meet at the International School of Minnesota during the robotics season. Contact us by email to schedule a visit or ask for current meeting details.</p>
  </section>

  <!-- Response Time -->
  <section class="text-center text-sm text-gray-500 dark:text-gray-400">
    <p>We typically respond to inquiries within 48 hours during the school year.</p>
  </section>
</div>
