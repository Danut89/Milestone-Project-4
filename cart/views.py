from decimal import Decimal
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import stripe

from shop.models import Product
from orders.models import Order, OrderItem
from profiles.models import UserProfile
from .models import CartItem
from .forms import CheckoutForm

stripe.api_key = settings.STRIPE_SECRET_KEY


# 📌 Helper to calculate cart total
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


# ✅ Checkout view – render form and save order after PaymentIntent success
@login_required
def checkout_view(request):
    items_qs = CartItem.objects.filter(user=request.user).select_related('product')
    cart = {
        str(item.product.id): {
            'name': item.product.name,
            'price': str(item.product.price),
            'quantity': item.quantity,
            'image_url': item.product.image.url if item.product.image else '',
        } for item in items_qs
    }

    # 🛑 Redirect if cart is empty
    if not cart:
        messages.warning(request, "Your cart is empty.")
        return redirect('view_cart')

    # ✅ Save the order after Stripe confirms payment
    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            cleaned = form.cleaned_data
            total = calculate_cart_total(cart)

            # Save the order
            order = Order.objects.create(
                user=request.user,
                full_name=cleaned['full_name'],
                email=cleaned['email'],
                phone_number=cleaned['phone_number'],
                address=f"{cleaned['address_line1']}, {cleaned['city']}",
                total_price=total,
                is_paid=True  # Because payment already confirmed via Stripe JS
            )

            for pid, item in cart.items():
                product = get_object_or_404(Product, pk=pid)
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=item['quantity'],
                    price=Decimal(item['price']),
                )

            # ✅ Clear cart
            CartItem.objects.filter(user=request.user).delete()

            messages.success(request, f"Thank you! Your order #{order.id} has been placed.")
            return render(request, 'cart/checkout_success.html', {
            'order': order,
                'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
            })

        else:
            messages.error(request, "❌ Please correct the errors below and try again.")

    else:
        form = CheckoutForm()
        if request.GET.get('use_saved_info') == 'on':
            try:
                user_profile = request.user.profile
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


# ✅ Create PaymentIntent (called from JS)
@csrf_exempt
@login_required
def create_payment_intent(request):
    if request.method == 'POST':
        items_qs = CartItem.objects.filter(user=request.user).select_related('product')
        cart = {
            str(item.product.id): {
                'name': item.product.name,
                'price': str(item.product.price),
                'quantity': item.quantity,
            } for item in items_qs
        }

        cart_total = sum(float(item['price']) * item['quantity'] for item in cart.values())

        intent = stripe.PaymentIntent.create(
            amount=int(cart_total * 100),  # amount in pence
            currency='gbp',
            metadata={'integration_check': 'accept_a_payment'},
        )

        return JsonResponse({'clientSecret': intent.client_secret})
