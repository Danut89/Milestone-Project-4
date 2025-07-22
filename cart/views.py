from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.http import JsonResponse
from decimal import Decimal
import stripe
from shop.models import Product
from orders.models import Order, OrderItem
from profiles.models import UserProfile
from .models import CartItem
from .forms import CheckoutForm


# 📌 Helper to calculate cart total for session-based carts
def calculate_cart_total(cart):
    return sum(float(item['price']) * item['quantity'] for item in cart.values())


# 🛒 Add product to cart
@require_POST
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.user.is_authenticated:
        item, created = CartItem.objects.get_or_create(user=request.user, product=product)
        if not created:
            item.quantity += 1
            item.save()
            messages.info(request, f"Updated quantity for '{product.name}' in your cart.")
        else:
            messages.success(request, f"Added '{product.name}' to your cart.")
    else:
        cart = request.session.get('cart', {})
        pid = str(product.id)
        if pid in cart:
            cart[pid]['quantity'] += 1
            messages.info(request, f"Updated quantity for '{product.name}' in your cart.")
        else:
            cart[pid] = {
                'name': product.name,
                'price': str(product.price),
                'quantity': 1,
                'image_url': product.image.url if product.image else '',
            }
            messages.success(request, f"Added '{product.name}' to your cart.")
        request.session['cart'] = cart

    return redirect('view_cart')


# 🛍️ View cart
def view_cart(request):
    cart_items = []
    total = Decimal('0.00')

    if request.user.is_authenticated:
        items = CartItem.objects.filter(user=request.user).select_related('product')
        for item in items:
            subtotal = item.product.price * item.quantity
            total += subtotal
            cart_items.append({
                'product': item.product,
                'quantity': item.quantity,
                'subtotal': subtotal,
            })
    else:
        cart = request.session.get('cart', {})
        for pid, data in cart.items():
            product = get_object_or_404(Product, pk=pid)
            subtotal = product.price * data['quantity']
            total += subtotal
            cart_items.append({
                'product': product,
                'quantity': data['quantity'],
                'subtotal': subtotal,
            })

    return render(request, 'cart/cart.html', {
        'cart_items': cart_items,
        'cart_total': total
    })


# ❌ Remove from cart
@require_POST
def remove_from_cart(request, product_id):
    if request.user.is_authenticated:
        item = CartItem.objects.filter(user=request.user, product_id=product_id).first()
        if item:
            product_name = item.product.name
            item.delete()
            messages.warning(request, f"Removed '{product_name}' from your cart.")
    else:
        cart = request.session.get('cart', {})
        pid = str(product_id)
        if pid in cart:
            product_name = cart[pid]['name']
            del cart[pid]
            request.session['cart'] = cart
            messages.warning(request, f"Removed '{product_name}' from your cart.")
    return redirect('view_cart')


@login_required
def checkout_view(request):
    # Get cart items
    items_qs = CartItem.objects.filter(user=request.user).select_related('product')
    cart = {
        str(item.product.id): {
            'name': item.product.name,
            'price': str(item.product.price),
            'quantity': item.quantity,
            'image_url': item.product.image.url if item.product.image else '',
        } for item in items_qs
    }

    # Handle post-payment success redirect
    if request.GET.get('success') == 'true':
        order_id = request.session.get('order_id')
        if order_id:
            order = get_object_or_404(Order, id=order_id, user=request.user)
            if not order.is_paid:
                order.is_paid = True
                order.save()
            CartItem.objects.filter(user=request.user).delete()
            request.session.pop('order_id', None)
            messages.success(request, f"Thank you! Your order #{order.id} has been confirmed.")
            return render(request, 'cart/checkout.html', {
                'order': order,
                'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
            })

        messages.warning(request, "We couldn't confirm your order.")
        return redirect('view_cart')

    # 🛑 Redirect if cart is empty
    if not cart:
        messages.warning(request, "Your cart is empty.")
        return redirect('view_cart')

    # ✅ Default form instance
    form = CheckoutForm()

    # ✅ Pre-fill form if checkbox is ticked
    if request.GET.get('use_saved_info') == 'on':
        try:
            user_profile = request.user.userprofile
            form = CheckoutForm(initial={
                'full_name': user_profile.default_full_name,
                'email': user_profile.default_email,
                'phone_number': user_profile.default_phone_number,
                'address_line1': user_profile.default_address_line1,
                'address_line2': user_profile.default_address_line2,
                'city': user_profile.default_city,
                'postcode': user_profile.default_postcode,
                'country': user_profile.default_country,
            })
        except UserProfile.DoesNotExist:
            messages.warning(request, "No saved delivery info found.")

    total = calculate_cart_total(cart)

    return render(request, 'cart/checkout.html', {
        'cart': cart,
        'cart_total': total,
        'form': form,
        'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
    })




# 🔐 Stripe config
stripe.api_key = settings.STRIPE_SECRET_KEY


# 🔁 Create Stripe checkout session
@login_required
@require_POST
def create_checkout_session(request):
    items_qs = CartItem.objects.filter(user=request.user).select_related('product')
    if not items_qs.exists():
        return JsonResponse({'error': 'Your cart is empty.'}, status=400)

    cart = {
        str(item.product.id): {
            'name': item.product.name,
            'price': str(item.product.price),
            'quantity': item.quantity,
        } for item in items_qs
    }

    total = sum(Decimal(item['price']) * item['quantity'] for item in cart.values())
    delivery = request.session.get('delivery_info', {})

    order = Order.objects.create(
        user=request.user,
        full_name=delivery.get('full_name', request.user.get_full_name() or "Guest"),
        email=delivery.get('email', request.user.email),
        address=delivery.get('address_line1', '') + ", " + delivery.get('city', ''),
        total_price=total,
    )

    for pid, item in cart.items():
        product = get_object_or_404(Product, pk=pid)
        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=item['quantity'],
            price=Decimal(item['price']),
        )

    request.session['order_id'] = order.id

    line_items = [
        {
            'price_data': {
                'currency': 'gbp',
                'product_data': {'name': item['name']},
                'unit_amount': int(float(item['price']) * 100),
            },
            'quantity': item['quantity'],
        }
        for item in cart.values()
    ]

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        customer_email=delivery.get('email'),
        shipping_address_collection={'allowed_countries': ['GB', 'RO']},
        success_url=request.build_absolute_uri('/cart/checkout/?success=true'),
        cancel_url=request.build_absolute_uri('/cart/checkout/?canceled=true'),
    )

    order.stripe_payment_id = session.id
    order.save()

    return JsonResponse({'id': session.id})




