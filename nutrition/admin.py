from django.contrib import admin
from .models import MealPlan, MealPlanDay, Recipe, Wishlist

# Register your models here.



admin.site.register(Wishlist)


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

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'prep_time_minutes', 'calories', 'author', 'created_at')
    search_fields = ('title', 'ingredients', 'instructions')
    list_filter = ('created_at', 'author')
    fieldsets = (
        (None, {
            'fields': ('title', 'ingredients', 'instructions', 'prep_time_minutes', 'image', 'author')
        }),
        ('Nutritional Info', {
            'fields': ('calories', 'protein', 'carbs', 'fat'),
            'classes': ('collapse',),  # Optional: collapsible section
        }),
    )

