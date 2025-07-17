document.addEventListener("DOMContentLoaded", function () {
  const stripe = Stripe(STRIPE_PUBLIC_KEY); // make sure you pass this in template context
  const button = document.getElementById("stripe-checkout-btn");
  const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

  if (button) {
    button.addEventListener("click", function () {
      fetch("/cart/create-checkout-session/", {
        method: "POST",
        headers: {
          "X-CSRFToken": csrfToken,
          "Content-Type": "application/json"
        },
      })
      .then(response => response.json())
      .then(data => {
        return stripe.redirectToCheckout({ sessionId: data.id });
      })
      .catch(error => {
        console.error("Stripe Checkout error:", error);
        alert("Checkout failed.");
      });
    });
  }
});

