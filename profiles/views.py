from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from itertools import chain

from .forms import UserUpdateForm, UserProfileForm
from profiles.models import UserProfile
from orders.models import Order
from nutrition.models import Wishlist, Recipe, MealPlan


@login_required
def dashboard(request):
    saved_recipes = Wishlist.objects.filter(user=request.user, recipe__isnull=False)
    saved_meal_plans = Wishlist.objects.filter(user=request.user, meal_plan__isnull=False)
    user = request.user
    profile = user.profile

    activities = []

    if not profile.hide_recent_activity:
        orders = Order.objects.filter(user=user).order_by('-created_at')[:3]
        recipes = Recipe.objects.filter(author=user).order_by('-created_at')[:3]
        meal_plans = MealPlan.objects.filter(created_by=user).order_by('-created_at')[:3]

        activities = sorted(
            chain(
                [{'type': 'order', 'item': order, 'date': order.created_at} for order in orders],
                [{'type': 'recipe', 'item': recipe, 'date': recipe.created_at} for recipe in recipes],
                [{'type': 'mealplan', 'item': plan, 'date': plan.created_at} for plan in meal_plans],
            ),
            key=lambda x: x['date'],
            reverse=True
        )

    return render(request, 'profiles/dashboard.html', {
        'saved_recipes': saved_recipes,
        'saved_meal_plans': saved_meal_plans,
        'activities': activities,
    })


@login_required
def toggle_recent_activity_visibility(request):
    profile = request.user.profile
    profile.hide_recent_activity = not profile.hide_recent_activity
    profile.save()

    status = "hidden" if profile.hide_recent_activity else "visible"
    messages.success(request, f"Recent activity is now {status}.")
    return redirect('settings_view')


@login_required
def settings_view(request):
    return render(request, 'profiles/settings.html')


@login_required
def edit_info_view(request):
    user = request.user
    profile = user.profile

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(
                request,
                'Your personal information was updated successfully!'
            )
            return redirect('settings_view')
    else:
        user_form = UserUpdateForm(instance=user)
        profile_form = UserProfileForm(instance=profile)

    return render(request, 'profiles/edit_info.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Keep user logged in
            messages.success(request, '✅ Password updated successfully.')
            return redirect('settings_view')
        else:
            messages.error(request, '⚠️ Please correct the errors below.')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'profiles/change_password.html', {'form': form})
