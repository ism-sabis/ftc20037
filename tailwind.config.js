/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./_layouts/**/*.html",
    "./_includes/**/*.html",
    "./*.html",
    "./*.md",
    "./seasons/**/*.html",
    "./seasons/**/*.md",
    "./docs/**/*.html",
    "./docs/**/*.md",
    "./_posts/**/*.md",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        // Precision Engineering — Deep Navy + Red Accent
        primary: {
          DEFAULT: '#0B1426', // Deep navy (team jersey)
          light: '#1a2744',
          dark: '#060d18',
          highlight: '#030710',
        },
        accent: {
          DEFAULT: '#DC2626', // Vibrant red (energy, from team jerseys)
          light: '#EF4444',   // Brighter red for highlights
          dark: '#991B1B',    // Dark red for hover states on dark bg
        },
        secondary: {
          DEFAULT: '#F57E25', // FIRST Orange
          light: '#f79b54',
          dark: '#d96a1f',
        },
        success: {
          DEFAULT: '#28a745',
          light: '#48c664',
          dark: '#228e3b',
        },
        info: {
          DEFAULT: '#17a2b8',
          light: '#3dbfd3',
          dark: '#148a9c',
        },
        warning: {
          DEFAULT: '#f0b37e',
          light: '#f5c8a0',
          dark: '#cc986b',
        },
        danger: {
          DEFAULT: '#dc3545',
          light: '#e4606d',
          dark: '#bb2d3b',
        },
        muted: '#6c757d',
        light: '#f8f9fa',
        dark: '#212529',
      },
      letterSpacing: {
        tighter: '-0.03em',
      },
      fontFamily: {
        sans: ['system-ui', '-apple-system', "BlinkMacSystemFont", "'Segoe UI'", 'Roboto', 'sans-serif'],
        mono: ["'JetBrains Mono'", "'Fira Code'", 'SFMono-Regular', 'Menlo', 'Monaco', 'Consolas', 'monospace'],
      },
    },
  },
  plugins: [],
}
