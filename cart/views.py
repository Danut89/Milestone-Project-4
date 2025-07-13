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
from .forms import CheckoutForm
from profiles.models import UserProfile
from cart.forms import CheckoutForm



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

    # ✅ Handle Stripe success return
    if request.GET.get('success') == 'true':
        order_id = request.session.get('order_id')
        if order_id:
            order = get_object_or_404(Order, id=order_id, user=request.user)

            # ✅ Mark the order as paid (if not already)
            if not order.is_paid:
                order.is_paid = True
                order.save()

            # ✅ Clear cart and order ID from session
            request.session['cart'] = {}
            if 'order_id' in request.session:
                del request.session['order_id']

            messages.success(request, f"Thank you! Your order #{order.id} has been confirmed.")
            return render(request, 'cart/checkout.html', {
                'order': order,
                'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
            })

        messages.warning(request, "We couldn't confirm your order. Please contact support.")
        return redirect('view_cart')

    # ✅ Redirect if cart is empty
    if not cart:
        messages.warning(request, "Your cart is empty.")
        return redirect('view_cart')

    # 🧾 Pre-fill form with user profile data
    profile = getattr(request.user, 'userprofile', None)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # ✅ Store delivery info in session
            request.session['delivery_info'] = {
                'full_name': data['full_name'],
                'email': data['email'],
                'phone_number': data['phone_number'],
                'address_line1': data['address_line1'],
                'address_line2': data['address_line2'],
                'city': data['city'],
                'postcode': data['postcode'],
                'country': data['country'],
            }

            messages.success(request, "Delivery information received.")
            return redirect('create_checkout_session')
    else:
        initial_data = {}
        if request.GET.get('use_saved_info') == 'on' and profile:
            initial_data = {
                'full_name': profile.default_full_name,
                'email': profile.default_email,
                'phone_number': profile.default_phone_number,
                'address_line1': profile.default_address_line1,
                'address_line2': profile.default_address_line2,
                'city': profile.default_city,
                'postcode': profile.default_postcode,
                'country': profile.default_country,
            }

        form = CheckoutForm(initial=initial_data)

    total = calculate_cart_total(cart)

    return render(request, 'cart/checkout.html', {
        'cart': cart,
        'cart_total': total,
        'form': form,
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

    # ✅ Get delivery info from session (submitted via form)
    delivery = request.session.get('delivery_info', {})

    # ⚠️ Create Order in DB
    order = Order.objects.create(
        user=request.user,
        full_name=delivery.get('full_name', request.user.get_full_name() or "Guest"),
        email=delivery.get('email', request.user.email),
        address=delivery.get('address_line1', '') + ", " + delivery.get('city', ''),
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

        # ✅ Create Stripe checkout session with customer & shipping info
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        customer_email=delivery.get('email'),
        shipping_address_collection={
            'allowed_countries': ['GB', 'RO'],
        },
        success_url=request.build_absolute_uri('/cart/checkout/?success=true'),
        cancel_url=request.build_absolute_uri('/cart/checkout/?canceled=true'),
    )

    # ✅ Save Stripe session ID to the order
    order.stripe_payment_id = session.id
    order.save()

    return JsonResponse({'id': session.id})
