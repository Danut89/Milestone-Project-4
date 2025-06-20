def cart_context(request):
    cart = request.session.get('cart', {})
    return {'cart_items_count': sum(item['quantity'] for item in cart.values())}
