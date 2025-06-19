from django.shortcuts import render
from .models import Product

# Create your views here.


def product_list(request):
    products = Product.objects.filter(available=True)
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