// ===============================
// 📦 Global Scripts - base.js
// ===============================

/**
 * 🔍 Global Search Validation
 * Prevents empty search submissions and adds inline validation styling.
 */
document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('global-search-form');
  const input = document.getElementById('global-search-input');

  if (!form || !input) return;

  form.addEventListener('submit', function (e) {
    if (!input.value.trim()) {
      e.preventDefault();
      input.classList.add('is-invalid');
    } else {
      input.classList.remove('is-invalid');
    }
  });
});

/**
 * ✨ Animate .glass-card elements when they come into view
 */
document.addEventListener('DOMContentLoaded', () => {
  const cards = document.querySelectorAll('.glass-card');

  if (!cards.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('animate');
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.3,
  });

  cards.forEach((card) => observer.observe(card));
});

/**
 * 📢 Show Django messages as Bootstrap toasts
 * Skips wishlist toast (handled separately).
 */
document.addEventListener('DOMContentLoaded', () => {
  const toastEls = document.querySelectorAll('.toast');

  toastEls.forEach((toastEl) => {
    if (toastEl.id === 'wishlistToast') return;
    const toast = new bootstrap.Toast(toastEl, { delay: 4000 });
    toast.show();
  });
});

/**
 * ❤️ Wishlist Toggle Logic
 * Handles save/remove from wishlist via AJAX.
 */
document.addEventListener('DOMContentLoaded', () => {
  const btn = document.getElementById('wishlist-btn');
  const toastEl = document.getElementById('wishlistToast');
  const toastBody = document.getElementById('toast-body');

  if (!btn || !toastEl || !toastBody) return;

  btn.addEventListener('click', function () {
    const itemId = btn.dataset.id;
    const itemType = btn.dataset.type;

    fetch('/nutrition/toggle-wishlist/', {
      method: 'POST',
      headers: {
        'X-CSRFToken': csrfToken,
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: `id=${itemId}&type=${itemType}`,
    })
    .then((response) => response.json())
    .then((data) => {
      if (data.status === 'added') {
        btn.classList.remove('btn-outline-danger');
        btn.classList.add('btn-danger');
        btn.innerHTML = `<i class="fas fa-heart me-2"></i> Remove from Wishlist`;
        toastEl.classList.replace('bg-danger', 'bg-success');
        toastBody.textContent = '❤️ Item added to your wishlist!';
      } else if (data.status === 'removed') {
        btn.classList.remove('btn-danger');
        btn.classList.add('btn-outline-danger');
        btn.innerHTML = `<i class="fas fa-heart me-2"></i> Save to Wishlist`;
        toastEl.classList.replace('bg-success', 'bg-danger');
        toastBody.textContent = '💔 Item removed from your wishlist.';
      }

      const toast = new bootstrap.Toast(toastEl);
      toast.show();
    })
    .catch((error) => {
      console.error('Wishlist toggle error:', error);
    });
  });
});
