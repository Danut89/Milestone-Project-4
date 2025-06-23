from django.contrib import admin
from .models import MealPlan, MealPlanDay, Recipe, Supplement

# Register your models here.

admin.site.register(MealPlan)
admin.site.register(MealPlanDay)
admin.site.register(Recipe)
admin.site.register(Supplement)
