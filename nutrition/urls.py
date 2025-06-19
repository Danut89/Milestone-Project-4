from django.urls import path
from . import views

urlpatterns = [
    path('meal-plans/', views.meal_plans, name='meal_plans'),
    path('recipes/', views.recipes_list, name='recipes'),
    path('supplements/', views.supplements_list, name='supplements'),
]

