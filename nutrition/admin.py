from django.contrib import admin
from .models import MealPlan, MealPlanDay, Recipe, Supplement

# Register your models here.


admin.site.register(Recipe)
admin.site.register(Supplement)


# Inline model for MealPlanDay
class MealPlanDayInline(admin.TabularInline):  # Or use StackedInline if you want
    model = MealPlanDay
    extra = 1  # Show one extra empty fieldset for adding a new day
    fields = ['day_number', 'description']
    ordering = ['day_number']

# Customize MealPlan admin to show days inline
@admin.register(MealPlan)
class MealPlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'calories', 'duration_days', 'created_at', 'created_by')
    search_fields = ('title', 'description')
    list_filter = ('created_at',)
    inlines = [MealPlanDayInline]


