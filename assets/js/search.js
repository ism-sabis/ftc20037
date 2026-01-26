/**
 * Client-side search functionality for Robo-Folio
 * Searches blog posts and documentation
 */

(function() {
  let searchIndex = [];
  let searchInput = document.getElementById('search-input');
  let searchResults = document.getElementById('search-results');

  // Load search index
  async function loadSearchIndex() {
    try {
      const response = await fetch('/search.json');
      searchIndex = await response.json();
    } catch (error) {
      console.error('Failed to load search index:', error);
    }
  }

  // Simple search function
  function search(query) {
    if (!query || query.length < 2) return [];

    const terms = query.toLowerCase().split(/\s+/);

    return searchIndex.filter(item => {
      const searchText = `${item.title} ${item.content} ${item.tags || ''}`.toLowerCase();
      return terms.every(term => searchText.includes(term));
    }).slice(0, 10); // Limit to 10 results
  }

  // Highlight matching terms
  function highlight(text, query) {
    const terms = query.toLowerCase().split(/\s+/);
    let result = text;

    terms.forEach(term => {
      const regex = new RegExp(`(${term})`, 'gi');
      result = result.replace(regex, '<mark class="bg-accent/30 px-0.5 rounded">$1</mark>');
    });

    return result;
  }

  // Render search results
  function renderResults(results, query) {
    if (!searchResults) return;

    if (results.length === 0) {
      searchResults.innerHTML = `
        <div class="p-4 text-center text-[var(--color-text-muted)]">
          No results found for "${query}"
        </div>
      `;
      searchResults.classList.remove('hidden');
      return;
    }

    const html = results.map(item => `
      <a href="${item.url}" class="block p-4 hover:bg-[var(--color-surface)] border-b border-[var(--color-border)] last:border-b-0">
        <h4 class="font-medium">${highlight(item.title, query)}</h4>
        <p class="text-sm text-[var(--color-text-muted)] line-clamp-2 mt-1">
          ${highlight(item.excerpt || item.content.substring(0, 150), query)}...
        </p>
        <span class="text-xs text-primary mt-2 inline-block">${item.type}</span>
      </a>
    `).join('');

    searchResults.innerHTML = html;
    searchResults.classList.remove('hidden');
  }

  // Hide results
  function hideResults() {
    if (searchResults) {
      searchResults.classList.add('hidden');
    }
  }

  // Initialize search
  if (searchInput) {
    loadSearchIndex();

    let debounceTimer;
    searchInput.addEventListener('input', (e) => {
      clearTimeout(debounceTimer);
      debounceTimer = setTimeout(() => {
        const query = e.target.value.trim();
        if (query.length >= 2) {
          const results = search(query);
          renderResults(results, query);
        } else {
          hideResults();
        }
      }, 300);
    });

    // Keyboard navigation
    let selectedIndex = -1;
    searchInput.addEventListener('keydown', (e) => {
      const items = searchResults?.querySelectorAll('a') || [];

      if (e.key === 'ArrowDown') {
        e.preventDefault();
        selectedIndex = Math.min(selectedIndex + 1, items.length - 1);
        items.forEach((item, i) => {
          item.classList.toggle('bg-[var(--color-surface)]', i === selectedIndex);
        });
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        selectedIndex = Math.max(selectedIndex - 1, 0);
        items.forEach((item, i) => {
          item.classList.toggle('bg-[var(--color-surface)]', i === selectedIndex);
        });
      } else if (e.key === 'Enter' && selectedIndex >= 0 && items[selectedIndex]) {
        e.preventDefault();
        window.location.href = items[selectedIndex].href;
      } else if (e.key === 'Escape') {
        hideResults();
        searchInput.blur();
      }
    });

    // Close on click outside
    document.addEventListener('click', (e) => {
      if (!searchInput.contains(e.target) && !searchResults?.contains(e.target)) {
        hideResults();
      }
    });
  }
})();
