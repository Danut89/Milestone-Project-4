from django.shortcuts import render, get_object_or_404
from .models import MealPlan, Recipe, Supplement
from django.core.paginator import Paginator

def nutrition_home(request):
    return render(request, 'nutrition/home.html')

def meal_plans(request):
    all_plans = MealPlan.objects.all()
    paginator = Paginator(all_plans, 6)  # Display 6 per page
    page_number = request.GET.get('page')
    plans = paginator.get_page(page_number)
    return render(request, 'nutrition/meal_plans.html', {'plans': plans})


def meal_plan_detail(request, pk):
    meal_plan = get_object_or_404(MealPlan, pk=pk)
    days = meal_plan.days.all().order_by('day_number')
    return render(request, 'nutrition/meal_plan_detail.html', {
        'meal_plan': meal_plan,
        'days': days,
    })

def recipes_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'nutrition/recipes.html', {'recipes': recipes})

def supplements_list(request):
    supplements = Supplement.objects.all()
    return render(request, 'nutrition/supplements.html', {'supplements': supplements})


