from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from .models import Product
from .forms import ProductForm
import random


# ✅ Show all available products
def all_products(request):
    product_list = Product.objects.filter(available=True)

    # Sorting logic
    sort = request.GET.get('sort')
    if sort == 'price_asc':
        product_list = product_list.order_by('price')
    elif sort == 'price_desc':
        product_list = product_list.order_by('-price')
    elif sort == 'name_asc':
        product_list = product_list.order_by('name')
    elif sort == 'name_desc':
        product_list = product_list.order_by('-name')
    elif sort == 'newest':
        product_list = product_list.order_by('-created')

    paginator = Paginator(product_list, 6)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    return render(request, 'shop/product_list.html', {
        'products': products,
        'current_sort': sort,
    })


# ✅ Dynamic category view
def products_by_category(request, category):
    sort_option = request.GET.get('sort', '')
    product_list = Product.objects.filter(
        category__iexact=category,
        available=True
    )

    if sort_option == 'price_asc':
        product_list = product_list.order_by('price')
    elif sort_option == 'price_desc':
        product_list = product_list.order_by('-price')
    elif sort_option == 'name_asc':
        product_list = product_list.order_by('name')
    elif sort_option == 'name_desc':
        product_list = product_list.order_by('-name')
    elif sort_option == 'newest':
        product_list = product_list.order_by('-created')

    paginator = Paginator(product_list, 6)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    return render(request, 'shop/category_products.html', {
        'products': products,
        'category_name': category.capitalize(),
        'current_sort': sort_option,
    })


# ✅ Product detail page
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    related_products = Product.objects.exclude(id=product.id).filter(available=True)
    related_products = random.sample(
        list(related_products),
        min(len(related_products), 3)
    )

    return render(request, 'shop/product_detail.html', {
        'product': product,
        'related_products': related_products,
    })


# ✅ Superuser-only check
def is_superuser(user):
    return user.is_superuser


# ✅ Edit product – superusers only
@login_required
@user_passes_test(is_superuser)
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)

    return render(request, 'shop/edit_product.html', {
        'form': form,
        'product': product
    })


# ✅ Delete product – superusers only
@login_required
@user_passes_test(is_superuser)
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('all_products')

    return render(request, 'shop/delete_product.html', {'product': product})
