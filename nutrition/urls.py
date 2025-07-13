from django.urls import path
from . import views

app_name = 'nutrition'

urlpatterns = [
    path('', views.nutrition_home, name='nutrition'),
    path('meal-plans/', views.meal_plans, name='meal_plans'),
    path('recipes/', views.recipes_list, name='recipes'),
    path('recipes/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('meal-plans/<int:pk>/', views.meal_plan_detail, name='meal_plan_detail'),
    path('toggle-wishlist/', views.toggle_wishlist, name='toggle_wishlist'),
    path('recipes/add/', views.add_recipe, name='add_recipe'),
    path('recipes/<int:pk>/edit/', views.edit_recipe, name='edit_recipe'),
    path('recipes/<int:pk>/delete/', views.delete_recipe, name='delete_recipe'),
]




