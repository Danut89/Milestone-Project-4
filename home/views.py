from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from shop.models import Product
from nutrition.models import MealPlan, Recipe
from django.shortcuts import redirect
from django.http import HttpResponse
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
        messages.success(request, "Thanks for contacting us! We'll get back to you soon.")
        return redirect('contact')

    return render(request, 'home/contact.html')









def global_search(request):
    query = request.GET.get('q', '').lower().strip()

    # Simple keyword mapping
    if 'meal' in query or 'plan' in query:
        return redirect('nutrition:meal_plans')  # Adjust name if needed
    elif 'recipe' in query:
        return redirect('nutrition:recipes')  
    elif 'shop' in query or 'product' in query:
        return redirect('product_list')  # Adjust name if needed
    elif 'cart' in query:
        return redirect('view_cart')
    elif 'dashboard' in query or 'account' in query:
        return redirect('dashboard')
    elif 'vegan' in query or 'weight' in query or 'protein' in query:
        return redirect(f"/nutrition/recipes/?tag={query}")  # Simple tag simulation
    else:
        return HttpResponse("Sorry, we couldn't find what you're looking for.")

