from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('equipment/', views.equipment_list, name='equipment'),
    path('clothing/', views.clothing_list, name='clothing'),
    path('supplements/', views.supplements_list, name='supplements'),
]
