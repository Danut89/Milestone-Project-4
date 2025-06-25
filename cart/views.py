from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product
from orders.models import Order, OrderItem
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from decimal import Decimal

# 📌 Helper function to calculate total
def calculate_cart_total(cart):
    return sum(float(item['price']) * item['quantity'] for item in cart.values())

# 🛒 Add product to cart
@require_POST
@login_required
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    product = get_object_or_404(Product, pk=product_id)
    product_id_str = str(product.id)

    if product_id_str in cart:
        cart[product_id_str]['quantity'] += 1
        messages.info(request, f"Updated quantity for '{product.name}' in your cart.")
    else:
        cart[product_id_str] = {
            'name': product.name,
            'price': str(product.price),
            'quantity': 1,
        }
        messages.success(request, f"Added '{product.name}' to your cart.")

    request.session['cart'] = cart
    return redirect('view_cart')

# 🛍️ View Cart Contents
@login_required
def view_cart(request):
    cart = request.session.get('cart', {})
    total = calculate_cart_total(cart)

    return render(request, 'cart/cart.html', {
        'cart': cart,
        'cart_total': total,
    })

# ❌ Remove product from cart
@require_POST
@login_required
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)

    if product_id_str in cart:
        product_name = cart[product_id_str]['name']
        del cart[product_id_str]
        request.session['cart'] = cart
        messages.warning(request, f"Removed '{product_name}' from your cart.")

    return redirect('view_cart')

# 💳 Checkout view (creates order)
@login_required
def checkout(request):
    cart = request.session.get('cart', {})

    if not cart:
        messages.info(request, "Your cart is empty.")
        return redirect('view_cart')

    total = calculate_cart_total(cart)

    # Create the order
    order = Order.objects.create(
        user=request.user,
        total_price=Decimal(str(total))
    )

    # Create each order item
    for product_id_str, item in cart.items():
        OrderItem.objects.create(
            order=order,
            product_id=int(product_id_str),
            quantity=item['quantity'],
            price=Decimal(str(item['price']))
        )

    # Clear cart and confirm success
    request.session['cart'] = {}
    messages.success(request, "Your order has been placed successfully!")

    return render(request, 'cart/checkout.html', {
        'order': order
    })
