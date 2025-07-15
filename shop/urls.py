from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('category/<str:category>/', views.products_by_category, name='products_by_category'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('<int:pk>/edit/', views.edit_product, name='edit_product'),
    path('<int:pk>/delete/', views.delete_product, name='delete_product'),
]
