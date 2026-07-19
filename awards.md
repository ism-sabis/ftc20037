---
layout: page
title: Awards
description: Our team's achievements and recognition over the years.
permalink: /awards/
---

<div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
  <!-- Header -->
  <section class="mb-12">
    <p class="text-sm font-semibold text-red-600 dark:text-red-400 uppercase tracking-wider mb-2">Achievements</p>
    <h1 class="text-3xl md:text-4xl font-bold text-gray-900 dark:text-white mb-4">Awards & Recognition</h1>
    <p class="text-gray-600 dark:text-gray-400">Our team's accomplishments and the recognition we've received for our hard work in engineering, outreach, and teamwork.</p>
  </section>

  <!-- All Awards -->
  <section class="mb-16">
    {% assign sorted_awards = site.data.awards | sort: "season" | reverse %}
    {% assign current_season = "" %}

    {% for award in sorted_awards %}
    {% if award.season != current_season %}
    {% assign current_season = award.season %}
    <h2 class="text-xl font-semibold text-gray-900 dark:text-white mt-8 mb-4 pb-2 border-b border-gray-100 dark:border-gray-700">{{ current_season }} Season</h2>
    {% endif %}

    <div class="bg-white dark:bg-gray-900 rounded-xl p-6 border border-gray-100 dark:border-gray-700 mb-4">
      <div class="flex items-start gap-4">
        <svg class="h-8 w-8 text-red-500 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"/></svg>
        <div class="flex-1">
          <h3 class="font-semibold text-lg text-gray-900 dark:text-white">{{ award.name }}</h3>
          <p class="text-sm font-medium text-red-600 dark:text-red-400 mt-1">{{ award.event }}</p>
          {% if award.description %}
          <p class="text-sm text-gray-600 dark:text-gray-400 mt-2">{{ award.description }}</p>
          {% endif %}
        </div>
      </div>
    </div>
    {% endfor %}
  </section>

  <!-- Award Criteria -->
  <section class="mb-16 bg-gray-50 dark:bg-gray-800 rounded-xl p-8 border border-gray-100 dark:border-gray-700">
    <p class="text-sm font-semibold text-red-600 dark:text-red-400 uppercase tracking-wider mb-2">About Awards</p>
    <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-6">FIRST Core Values Awards</h2>

    <div class="grid md:grid-cols-2 gap-4">
      <div class="bg-white dark:bg-gray-900 rounded-lg p-4 border border-gray-100 dark:border-gray-700">
        <h3 class="font-semibold text-gray-900 dark:text-white mb-1">Inspire Award</h3>
        <p class="text-sm text-gray-600 dark:text-gray-400">The highest honor, recognizing a team that best embodies the FIRST mission.</p>
      </div>

      <div class="bg-white dark:bg-gray-900 rounded-lg p-4 border border-gray-100 dark:border-gray-700">
        <h3 class="font-semibold text-gray-900 dark:text-white mb-1">Think Award</h3>
        <p class="text-sm text-gray-600 dark:text-gray-400">Excellence in engineering documentation and process.</p>
      </div>

      <div class="bg-white dark:bg-gray-900 rounded-lg p-4 border border-gray-100 dark:border-gray-700">
        <h3 class="font-semibold text-gray-900 dark:text-white mb-1">Connect Award</h3>
        <p class="text-sm text-gray-600 dark:text-gray-400">Outstanding outreach and community engagement.</p>
      </div>

      <div class="bg-white dark:bg-gray-900 rounded-lg p-4 border border-gray-100 dark:border-gray-700">
        <h3 class="font-semibold text-gray-900 dark:text-white mb-1">Innovate Award</h3>
        <p class="text-sm text-gray-600 dark:text-gray-400">Creative and effective robot design solutions.</p>
      </div>

      <div class="bg-white dark:bg-gray-900 rounded-lg p-4 border border-gray-100 dark:border-gray-700">
        <h3 class="font-semibold text-gray-900 dark:text-white mb-1">Control Award</h3>
        <p class="text-sm text-gray-600 dark:text-gray-400">Exceptional autonomous control.</p>
      </div>

      <div class="bg-white dark:bg-gray-900 rounded-lg p-4 border border-gray-100 dark:border-gray-700">
        <h3 class="font-semibold text-gray-900 dark:text-white mb-1">Motivate Award</h3>
        <p class="text-sm text-gray-600 dark:text-gray-400">Best team spirit and enthusiasm.</p>
      </div>

      <div class="bg-white dark:bg-gray-900 rounded-lg p-4 border border-gray-100 dark:border-gray-700 md:col-span-2 max-w-md">
        <h3 class="font-semibold text-gray-900 dark:text-white mb-1">Design Award</h3>
        <p class="text-sm text-gray-600 dark:text-gray-400">Outstanding robot aesthetics and industrial design.</p>
      </div>
    </div>
  </section>

  <!-- CTA -->
  <section class="text-center bg-red-50 dark:bg-red-950/30 rounded-xl p-8 border border-red-100 dark:border-red-900">
    <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-4">Want to help us earn more awards?</h2>
    <a href="{{ '/about/' | relative_url }}#join" class="inline-flex items-center px-6 py-2.5 bg-red-600 hover:bg-red-700 text-white font-medium rounded-lg transition-colors focus-visible:ring-2 focus-visible:ring-red-500 focus-visible:outline-none">
      Join Our Team
    </a>
  </section>
</div>
