from django.shortcuts import render, get_object_or_404
from .models import MealPlan, Recipe, Supplement, Wishlist
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

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

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    is_saved = False

    if request.user.is_authenticated:
        is_saved = Wishlist.objects.filter(user=request.user, recipe=recipe).exists()

    return render(request, 'nutrition/recipe_detail.html', {
        'recipe': recipe,
        'is_saved': is_saved
    })


def supplements_list(request):
    supplements = Supplement.objects.all()
    return render(request, 'nutrition/supplements.html', {'supplements': supplements})


@login_required
def add_to_wishlist(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    Wishlist.objects.get_or_create(user=request.user, recipe=recipe)
    return redirect('nutrition:recipe_detail', recipe_id=recipe.id)