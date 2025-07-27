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
    popular_products = Product.objects.filter(available=True)[:6]  # Adjust if you want filtering
    return render(request, 'home/index.html', {
        'popular_products': popular_products,
    })

@login_required
def dashboard(request):
    return render(request, 'home/dashboard.html')


def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if not name or not email or not message:
            error_msg = "All fields are required."
            if request.headers.get("X-Requested-With") == "XMLHttpRequest":
                return JsonResponse({"message": error_msg}, status=400)
            messages.error(request, error_msg)
            return redirect('contact')

        # Optional: save or send
        print(f"[CONTACT FORM] {name} ({email}): {message}")

        success_msg = "Thanks for contacting us! We’ll get back to you soon."

        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            return JsonResponse({"message": success_msg})
        
        messages.success(request, success_msg)
        return redirect('contact')

    return render(request, 'home/contact.html')


# ==============================
# 🔍 Global Search Functionality
def global_search(request):
    query = request.GET.get('q', '').lower().strip()

    if not query:
        messages.error(request, "Please enter a search term.")
        return redirect(request.META.get("HTTP_REFERER", reverse("home")))


    # === Dictionary-based keyword to view mappings ===
    basic_redirects = {
        'meal': 'nutrition:meal_plans',
        'plan': 'nutrition:meal_plans',
        'recipe': 'nutrition:recipes',
        'shop': 'all_products',
        'product': 'all_products',
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

    # === Exact match redirect (priority 1) ===
    product = Product.objects.filter(name__iexact=query).first()
    if product:
        return redirect('product_detail', slug=product.slug)

    recipe = Recipe.objects.filter(title__iexact=query).first()
    if recipe:
        return redirect('nutrition:recipe_detail', pk=recipe.pk)

    meal_plan = MealPlan.objects.filter(title__iexact=query).first()
    if meal_plan:
        return redirect('nutrition:meal_plan_detail', pk=meal_plan.pk)

    # === Partial match fallback (priority 2) ===
    products = Product.objects.filter(name__icontains=query)
    recipes = Recipe.objects.filter(title__icontains=query)
    meal_plans = MealPlan.objects.filter(title__icontains=query)

    if products.exists() or recipes.exists() or meal_plans.exists():
        return render(
            request,
            'home/global_search_results.html',
            {
                'products': products,
                'recipes': recipes,
                'meal_plans': meal_plans,
                'query': query,
            },
        )

    messages.warning(request, "No results found.")
    return redirect(request.META.get('HTTP_REFERER', 'home'))