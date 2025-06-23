from django.urls import path
from . import views

app_name = 'nutrition'

urlpatterns = [
    path('', views.nutrition_home, name='nutrition'),
    path('meal-plans/', views.meal_plans, name='meal_plans'),
    path('recipes/', views.recipes_list, name='recipes'),
    path('supplements/', views.supplements_list, name='supplements'),
    path('meal-plans/<int:pk>/', views.meal_plan_detail, name='meal_plan_detail'),
]




