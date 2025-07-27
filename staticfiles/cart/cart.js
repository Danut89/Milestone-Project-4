document.addEventListener("DOMContentLoaded", async function () {
  const stripe = Stripe(STRIPE_PUBLIC_KEY);  // from template context
  const elements = stripe.elements();
  const card = elements.create('card');
  card.mount('#card-element');

  const form = document.getElementById("checkout-form");
  const button = document.getElementById("checkout-btn");
  const spinner = document.getElementById("checkout-spinner");
  const buttonText = document.getElementById("checkout-btn-text");

  // Optional: store original text to restore later
  const originalText = buttonText.textContent = `Pay Now (£${button.dataset.total})`;
;

  // Get the PaymentIntent client_secret
  const intentRes = await fetch(CREATE_PAYMENT_INTENT_URL, {
    method: 'POST',
    headers: {
      "X-CSRFToken": CSRF_TOKEN,
    },
  });

  const { clientSecret } = await intentRes.json();

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = new FormData(form);
    const billingDetails = {
      name: formData.get('full_name'),
      email: formData.get('email'),
    };

    // Show spinner
    button.setAttribute("disabled", true);
    spinner.classList.remove("d-none");
    buttonText.textContent = "Processing...";

    const { error, paymentIntent } = await stripe.confirmCardPayment(clientSecret, {
      payment_method: {
        card: card,
        billing_details: billingDetails
      }
    });

    if (error) {
      // Restore button state
      button.removeAttribute("disabled");
      spinner.classList.add("d-none");
      buttonText.textContent = originalText;

      // Show error as toast
      const toastContainer = document.querySelector(".toast-container");
      const toastHTML = `
        <div class="toast align-items-center text-white bg-danger border-0 show" role="alert">
          <div class="d-flex">
            <div class="toast-body">${error.message}</div>
            <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
          </div>
        </div>
      `;
      toastContainer.insertAdjacentHTML("beforeend", toastHTML);
      new bootstrap.Toast(toastContainer.lastElementChild).show();
      return;
    }

    // Payment successful — submit to backend to create order
    form.submit();
  });
});

