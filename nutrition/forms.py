# nutrition/forms.py
from django import forms
from .models import MealPlan

class MealPlanForm(forms.ModelForm):
    class Meta:
        model = MealPlan
        fields = ['title', 'description', 'calories', 'duration_days']
