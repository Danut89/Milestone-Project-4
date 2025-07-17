from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver

from .models import CartItem


@receiver(user_logged_in)
def merge_cart_on_login(sender, user, request, **kwargs):
    """Merge any session cart items into the user's persistent cart on login."""
    session_cart = request.session.get('cart', {}) or {}
    for product_id, item in session_cart.items():
        cart_item, created = CartItem.objects.get_or_create(
            user=user,
            product_id=product_id,
            defaults={'quantity': item.get('quantity', 0)}
        )
        if not created:
            cart_item.quantity += item.get('quantity', 0)
            cart_item.save()
    # Clear session cart after merge
    request.session['cart'] = {}