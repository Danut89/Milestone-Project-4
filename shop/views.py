from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Product
from .forms import ProductForm


# ✅ Show all available products
def all_products(request):
    products = Product.objects.filter(available=True)
    return render(request, 'shop/product_list.html', {'products': products})


# ✅ Dynamic category view (Step 1.2)
def products_by_category(request, category):
    """Dynamically filter products by category name (case-insensitive)"""
    filtered_products = Product.objects.filter(category__iexact=category, available=True)
    context = {
        'products': filtered_products,
        'category_name': category.capitalize()
    }
    return render(request, 'shop/category_products.html', context)


# ✅ Product detail page
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})


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
