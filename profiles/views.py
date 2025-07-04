from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from nutrition.models import Recipe
from .models import RecipeWishlist

# Create your views here.



@login_required
def dashboard_view(request):
    saved_recipes = RecipeWishlist.objects.filter(user=request.user).select_related('recipe')
    return render(request, 'profiles/dashboard.html', {
        'saved_recipes': saved_recipes
    })


@login_required
def settings_view(request):
    return render(request, 'profiles/settings.html')



@login_required
def toggle_recipe_wishlist(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    wishlist_entry, created = RecipeWishlist.objects.get_or_create(user=request.user, recipe=recipe)

    if not created:
        wishlist_entry.delete()
        messages.info(request, f'Recipe "{recipe.title}" removed from your wishlist.')
    else:
        messages.success(request, f'Recipe "{recipe.title}" added to your wishlist.')

    return redirect('nutrition:recipe_detail', pk=recipe.id)