from django.shortcuts import render
from .models import MealPlan, Recipe, Supplement

def meal_plans(request):
    plans = MealPlan.objects.all()
    return render(request, 'nutrition/meal_plans.html', {'plans': plans})

def recipes_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'nutrition/recipes.html', {'recipes': recipes})

def supplements_list(request):
    supplements = Supplement.objects.all()
    return render(request, 'nutrition/supplements.html', {'supplements': supplements})

