from django.contrib import admin
from .models import MealPlan, Recipe, Supplement

# Register your models here.

admin.site.register(MealPlan)
admin.site.register(Recipe)
admin.site.register(Supplement)
