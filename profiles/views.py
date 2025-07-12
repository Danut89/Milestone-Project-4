from django.shortcuts import render, redirect
from nutrition.models import Wishlist  
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm
from django.contrib import messages
from .forms import UserUpdateForm, UserProfileForm

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





@login_required
def edit_info_view(request):
    user = request.user
    profile = user.userprofile

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your personal information was updated successfully!')
            return redirect('settings_view')
    else:
        user_form = UserUpdateForm(instance=user)
        profile_form = UserProfileForm(instance=profile)

    return render(request, 'profiles/edit_info.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })