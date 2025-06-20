from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('equipment/', views.equipment_list, name='equipment'),
    path('clothing/', views.clothing_list, name='clothing'),
    path('supplements/', views.supplements_list, name='supplements'),
    path('', views.all_products, name='product_list'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('<int:pk>/edit/', views.edit_product, name='edit_product'),
    path('<int:pk>/delete/', views.delete_product, name='delete_product'),
]
