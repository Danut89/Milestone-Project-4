from django.shortcuts import render
from nutrition.models import Wishlist  
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.




@login_required
def dashboard(request):
    saved_recipes = Wishlist.objects.filter(user=request.user, recipe__isnull=False)
    saved_meal_plans = Wishlist.objects.filter(user=request.user, meal_plan__isnull=False)

    return render(request, 'profiles/dashboard.html', {
        'saved_recipes': saved_recipes,
        'saved_meal_plans': saved_meal_plans,
    })

@login_required
def settings_view(request):
    return render(request, 'profiles/settings.html')
