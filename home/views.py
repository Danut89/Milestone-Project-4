from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from shop.models import Product
from nutrition.models import MealPlan, Recipe
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request, 'home/index.html')

@login_required
def dashboard(request):
    return render(request, 'home/dashboard.html')

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # You could save this info or send an email
        success_msg = "Thanks for contacting us! We'll get back to you soon."

        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            return JsonResponse({"message": success_msg})

        messages.success(request, success_msg)
        return redirect('contact')

    return render(request, 'home/contact.html')

def global_search(request):
    query = request.GET.get('q', '').lower().strip()

    # === Dictionary-based keyword to view mappings ===
    basic_redirects = {
        'meal': 'nutrition:meal_plans',
        'plan': 'nutrition:meal_plans',
        'recipe': 'nutrition:recipes',
        'shop': 'product_list',
        'product': 'product_list',
        'cart': 'view_cart',
        'dashboard': 'dashboard',
        'account': 'dashboard',
        'contact': 'contact',
    }

    for keyword, route_name in basic_redirects.items():
        if keyword in query:
            return redirect(route_name)

    # === Tags simulation (e.g., vegan, protein, etc.) ===
    tag_keywords = ['vegan', 'weight', 'protein']
    for tag in tag_keywords:
        if tag in query:
            return redirect(f"/nutrition/recipes/?tag={query}")

    # === Shop category redirection ===
    category_map = {
        'equipment': 'equipment',
        'clothing': 'clothing',
        'supplement': 'supplements',
        'supplements': 'supplements',
    }
    for keyword, category_slug in category_map.items():
        if keyword in query:
            return redirect('products_by_category', category=category_slug)

    # === Search for specific Meal Plan ===
    meal_plan = MealPlan.objects.filter(title__icontains=query).first()
    if meal_plan:
        return redirect('nutrition:meal_plan_detail', pk=meal_plan.id)

    # === Search for specific Recipe ===
    recipe = Recipe.objects.filter(title__icontains=query).first()
    if recipe:
        return redirect('nutrition:recipe_detail', pk=recipe.id)

    # === Search for specific Product ===
    product = Product.objects.filter(name__icontains=query).first()
    if product:
        return redirect('product_detail', pk=product.id)

    # === No match fallback ===
    return HttpResponse("Sorry, we couldn't find what you're looking for.")
