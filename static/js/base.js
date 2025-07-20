document.addEventListener("DOMContentLoaded", () => {
  const cards = document.querySelectorAll(".glass-card");

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("animate");
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.3,
  });

  cards.forEach((card) => observer.observe(card));
});
