from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('settings/', views.settings_view, name='settings'),
    path('wishlist/recipe/<int:recipe_id>/', views.toggle_recipe_wishlist, name='toggle_recipe_wishlist'),
]
