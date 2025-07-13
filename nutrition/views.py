from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.db import transaction
from django.urls import reverse
from .models import MealPlan, Recipe, Supplement, Wishlist
from .forms import RecipeForm  # Make sure to create this form if not already created

# ==============================
# 📄 Static & Listing Views
# ==============================

def nutrition_home(request):
    return render(request, 'nutrition/home.html')

def meal_plans(request):
    sort_option = request.GET.get('sort')

    all_plans = MealPlan.objects.all()

    if sort_option == 'newest':
        all_plans = all_plans.order_by('-created_at')
    elif sort_option == 'title_asc':
        all_plans = all_plans.order_by('title')
    elif sort_option == 'calories_asc':
        all_plans = all_plans.order_by('calories')
    elif sort_option == 'calories_desc':
        all_plans = all_plans.order_by('-calories')
    elif sort_option == 'duration_asc':
        all_plans = all_plans.order_by('duration_days')
    elif sort_option == 'duration_desc':
        all_plans = all_plans.order_by('-duration_days')

    paginator = Paginator(all_plans, 6)
    page_number = request.GET.get('page')
    plans = paginator.get_page(page_number)

    return render(request, 'nutrition/meal_plans.html', {
        'plans': plans,
        'current_sort': sort_option
    })


from django.db.models import Q

def recipes_list(request):
    sort_option = request.GET.get('sort', 'newest')
    
    # Default ordering
    sort_dict = {
        'newest': '-created_at',
        'title': 'title',
        'prep_time_asc': 'prep_time_minutes',
        'prep_time_desc': '-prep_time_minutes',
        'calories_asc': 'calories',
        'calories_desc': '-calories',
    }

    sort_by = sort_dict.get(sort_option, '-created_at')
    recipes = Recipe.objects.all().order_by(sort_by)

    # Pagination
    paginator = Paginator(recipes, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'current_sort': sort_option,
    }
    return render(request, 'nutrition/recipes.html', context)

def supplements_list(request):
    supplements = Supplement.objects.all()
    return render(request, 'nutrition/supplements.html', {'supplements': supplements})


# ==============================
# 🔍 Detail Views
# ==============================

def meal_plan_detail(request, pk):
    meal_plan = get_object_or_404(MealPlan, pk=pk)
    is_saved = False
    if request.user.is_authenticated:
        is_saved = Wishlist.objects.filter(user=request.user, meal_plan=meal_plan).exists()

    days = meal_plan.get_days
    
    return render(request, 'nutrition/meal_plan_detail.html', {
        'meal_plan': meal_plan,
        'is_saved': is_saved,
        'days': days
    })

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    is_saved = False
    if request.user.is_authenticated:
        is_saved = Wishlist.objects.filter(user=request.user, recipe=recipe).exists()
    return render(request, 'nutrition/recipe_detail.html', {
        'recipe': recipe,
        'is_saved': is_saved,
    })


# ==============================
# 💖 Wishlist Toggle View
# ==============================

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


# ==============================
# ✏️ CRUD Views for Recipes (TDD)
# ==============================

@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('nutrition:recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm()
    return render(request, 'nutrition/recipe_form.html', {'form': form})

@login_required
def edit_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk, author=request.user)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('nutrition:recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'nutrition/recipe_form.html', {'form': form})

#

from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Recipe, Wishlist
from django.db import transaction

def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    if request.user != recipe.author and not request.user.is_superuser:
        messages.error(request, "You don't have permission to delete this recipe.")
        return redirect("nutrition:recipe_detail", pk=pk)

    try:
        with transaction.atomic():
            # ✅ Step 1: Delete related wishlist entries
            Wishlist.objects.filter(recipe=recipe).delete()

            # ✅ Step 2: Delete the recipe
            recipe.delete()

        messages.success(request, "Recipe deleted successfully.")
        return redirect("nutrition:recipes")

    except Exception as e:
        print("Error while deleting:", e)
        messages.error(request, "An error occurred while deleting the recipe.")
        return redirect("nutrition:recipe_detail", pk=pk)






