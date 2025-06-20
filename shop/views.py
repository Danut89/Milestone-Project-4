from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm
from .forms import ProductForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from .forms import ProductForm



# Create your views here.


def all_products(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def equipment_list(request):
    products = Product.objects.filter(category='equipment')
    return render(request, 'shop/equipment.html', {'products': products})

def clothing_list(request):
    products = Product.objects.filter(category='clothing')
    return render(request, 'shop/clothing.html', {'products': products})

def supplements_list(request):
    products = Product.objects.filter(category='supplements')
    return render(request, 'shop/supplements.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})

# 🖊️ Edit product
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)

    return render(request, 'shop/edit_product.html', {'form': form, 'product': product})


# ❌ Delete product
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('all_products')  # Or to any list page you prefer

    return render(request, 'shop/delete_product.html', {'product': product})


# Only allow superusers (admins) for now
def is_superuser(user):
    return user.is_superuser


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
    return render(request, 'shop/edit_product.html', {'form': form, 'product': product})


@login_required
@user_passes_test(is_superuser)
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')  # or redirect to shop main
    return render(request, 'shop/delete_product.html', {'product': product})