from django.shortcuts import render, get_object_or_404
from .models import MealPlan, Recipe, Supplement, Wishlist
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.

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

    # Check if user has saved this meal plan
    is_saved = False
    if request.user.is_authenticated:
        is_saved = Wishlist.objects.filter(user=request.user, meal_plan=meal_plan).exists()

    return render(request, 'nutrition/meal_plan_detail.html', {
        'meal_plan': meal_plan,
        'is_saved': is_saved
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
        'is_saved': is_saved,
    })


def supplements_list(request):
    supplements = Supplement.objects.all()
    return render(request, 'nutrition/supplements.html', {'supplements': supplements})




@login_required
def toggle_wishlist(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        item_type = request.POST.get('type')
        item_id = request.POST.get('id')

        try:
            if item_type == 'recipe':
                recipe = Recipe.objects.get(id=item_id)
                wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, recipe=recipe)
                if not created:
                    wishlist_item.delete()
                    return JsonResponse({'status': 'removed'})
                return JsonResponse({'status': 'added'})

            elif item_type == 'meal_plan':
                plan = MealPlan.objects.get(id=item_id)
                wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, meal_plan=plan)
                if not created:
                    wishlist_item.delete()
                    return JsonResponse({'status': 'removed'})
                return JsonResponse({'status': 'added'})

        except (Recipe.DoesNotExist, MealPlan.DoesNotExist):
            return JsonResponse({'status': 'error', 'message': 'Item not found'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'})
