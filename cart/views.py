from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from shop.models import Product
from django.views.decorators.http import require_POST
from orders.models import Order, OrderItem
from django.contrib.auth.decorators import login_required
from decimal import Decimal

# Create your views here.


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    product = get_object_or_404(Product, pk=product_id)
    product_id_str = str(product.id)

    if product_id_str in cart:
        cart[product_id_str]['quantity'] += 1
    else:
        cart[product_id_str] = {
            'name': product.name,
            'price': str(product.price),
            'quantity': 1,
        }

    request.session['cart'] = cart
    return redirect('view_cart')

def view_cart(request):
    cart = request.session.get('cart', {})
    total = 0

    for item in cart.values():
        total += float(item['price']) * item['quantity']

    return render(request, 'cart/cart.html', {
        'cart': cart,
        'cart_total': total,
    })


@require_POST
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)

    if product_id_str in cart:
        del cart[product_id_str]
        request.session['cart'] = cart

    return redirect('view_cart')

@login_required
def checkout(request):
    cart = request.session.get('cart', {})

    if not cart:
        return redirect('view_cart')

    total = 0
    for item in cart.values():
        total += float(item['price']) * item['quantity']

    # Create the order
    order = Order.objects.create(
        user=request.user,
        total_price=Decimal(str(total))
    )

    # Create order items
    for product_id_str, item in cart.items():
        OrderItem.objects.create(
            order=order,
            product_id=int(product_id_str),
            quantity=item['quantity'],
            price=Decimal(str(item['price']))
        )

    # Clear the cart
    request.session['cart'] = {}

    return render(request, 'cart/checkout.html', {
        'order': order
    })