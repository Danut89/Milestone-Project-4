from django import forms
from .models import MealPlan, Recipe

# 🌱 Meal Plan Form
class MealPlanForm(forms.ModelForm):
    class Meta:
        model = MealPlan
        fields = ['title', 'description', 'calories', 'duration_days']

# 🍽️ Recipe Form
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'prep_time_minutes', 'ingredients', 'instructions', 'image', 'calories', 'protein', 'carbs', 'fat']

