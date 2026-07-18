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
        // Team Jersey Red + FIRST Orange Accent
        primary: {
          DEFAULT: '#DC2626', // Vibrant red from jerseys
          light: '#EF4444',
          dark: '#B91C1C',
          highlight: '#991B1B',
        },
        secondary: {
          DEFAULT: '#F57E25', // FIRST Orange (accent)
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
      fontFamily: {
        sans: ['Lato', 'Inter', 'system-ui', 'sans-serif'],
        mono: ['SFMono-Regular', 'Menlo', 'Monaco', 'Consolas', 'monospace'],
      },
    },
  },
  plugins: [],
}
