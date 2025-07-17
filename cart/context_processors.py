# 📦 Context processor for injecting cart item count into all templates
from django.db import models


def cart_context(request):
    """
    Adds the total quantity of items in the cart to the template context.
    Useful for displaying a live cart badge in the navbar.
    """
    if request.user.is_authenticated:
        from .models import CartItem
        cart_items_count = CartItem.objects.filter(user=request.user).aggregate(
            total=models.Sum('quantity')
        )['total'] or 0
    else:
        cart = request.session.get('cart', {})
        cart_items_count = sum(item.get('quantity', 0) for item in cart.values())
    return {
        'cart_items_count': cart_items_count
    }