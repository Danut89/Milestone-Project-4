from django.contrib import admin
from .models import Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'available')
    list_filter = ('category', 'available')
    search_fields = ('name', 'description', 'sku')