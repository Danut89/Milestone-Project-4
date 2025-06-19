from django.shortcuts import render
from .models import MealPlan

def meal_plans(request):
    plans = MealPlan.objects.all()
    return render(request, 'nutrition/meal_plans.html', {'plans': plans})


def recipes(request):
    return render(request, 'nutrition/recipes.html')

def supplements(request):
    return render(request, 'nutrition/supplements.html')

