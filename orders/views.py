from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Order
from django.shortcuts import get_object_or_404

# Create your views here.


from django.core.paginator import Paginator

@login_required
def order_history(request):
    # Get all orders for the logged-in user, newest first
    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    # Paginate orders: 10 per page
    paginator = Paginator(orders, 10)
    page_number = request.GET.get('page')
    page_orders = paginator.get_page(page_number)

    return render(request, 'orders/order_history.html', {
        'orders': page_orders,
        'most_recent_id': orders.first().id if orders else None,
    })




@login_required
def order_detail(request, order_id):
    # Make sure the user is only accessing their own orders
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})