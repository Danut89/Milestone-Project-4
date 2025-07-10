from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product
from orders.models import Order, OrderItem
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from decimal import Decimal
import stripe
from django.conf import settings
from django.http import JsonResponse

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
            'image_url': product.image.url if product.image else '',
        }
        messages.success(request, f"Added '{product.name}' to your cart.")

    request.session['cart'] = cart
    return redirect('view_cart')

# 🛍️ View Cart Contents
@login_required
def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = Decimal('0.00')

    for item_id, item_data in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        quantity = item_data['quantity'] if isinstance(item_data, dict) else item_data
        subtotal = product.price * quantity
        total += subtotal
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    context = {
        'cart_items': cart_items,
        'cart_total': total,
    }
    return render(request, 'cart/cart.html', context)


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

# 💳 Checkout view with user form and order creation
@login_required
def checkout_view(request):
    cart = request.session.get('cart', {})

    # ✅ Handle Stripe success redirect
    if request.GET.get('success') == 'true':
        order_id = request.session.get('order_id')
        if order_id:
            order = get_object_or_404(Order, id=order_id, user=request.user)

            # Clear cart and session
            request.session['cart'] = {}
            del request.session['order_id']

            return render(request, 'cart/checkout.html', {
                'order': order,
                'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
            })

        # If no order found, fallback
        messages.warning(request, "We couldn't confirm your order. Please contact support.")
        return redirect('view_cart')

    if not cart:
        messages.warning(request, "Your cart is empty.")
        return redirect('view_cart')

    total = calculate_cart_total(cart)
    return render(request, 'cart/checkout.html', {
        'cart': cart,
        'cart_total': total,
        'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
    })





stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
@require_POST
def create_checkout_session(request):
    cart = request.session.get('cart', {})
    if not cart:
        return JsonResponse({'error': 'Your cart is empty.'}, status=400)

    # ⚠️ Calculate total
    total = Decimal('0.00')
    for item in cart.values():
        total += Decimal(item['price']) * item['quantity']

    # ⚠️ Create Order in DB
    order = Order.objects.create(
        user=request.user,
        full_name=request.user.get_full_name() or "Guest",
        email=request.user.email,
        address="Stripe billing address placeholder",  # You can customize this later
        total_price=total
    )

    # ⚠️ Add order items
    for item_id, item in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=item['quantity'],
            price=Decimal(item['price'])
        )

    # ✅ Store order_id in session
    request.session['order_id'] = order.id

    # ✅ Prepare Stripe line items
    line_items = []
    for item in cart.values():
        line_items.append({
            'price_data': {
                'currency': 'gbp',
                'product_data': {
                    'name': item['name'],
                },
                'unit_amount': int(float(item['price']) * 100),
            },
            'quantity': item['quantity'],
        })

    # ✅ Create Stripe checkout session
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        success_url=request.build_absolute_uri('/cart/checkout/?success=true'),
        cancel_url=request.build_absolute_uri('/cart/checkout/?canceled=true'),
    )

    return JsonResponse({'id': session.id})

