from django.contrib import admin
from .models import MealPlan, MealPlanDay, Recipe, Wishlist

# ✅ Register Wishlist
admin.site.register(Wishlist)

# ✅ Inline model for MealPlanDay
class MealPlanDayInline(admin.TabularInline):
    model = MealPlanDay
    extra = 1
    fields = ['day_number', 'description']
    ordering = ['day_number']

# ✅ MealPlan Admin with inline MealPlanDays
@admin.register(MealPlan)
class MealPlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'calories', 'duration_days', 'created_at', 'created_by')
    search_fields = ('title', 'description')
    list_filter = ('created_at',)
    inlines = [MealPlanDayInline]

# ✅ Recipe Admin with Category Support
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'prep_time_minutes', 'calories', 'category', 'author', 'created_at')
    search_fields = ('title', 'ingredients', 'instructions')
    list_filter = ('category', 'created_at', 'author')
    fieldsets = (
        (None, {
            'fields': (
                'title',
                'description',  # ✅ Added description field
                'category',  # ✅ Added category field
                'ingredients',
                'instructions',
                'prep_time_minutes',
                'image',
                'author'
            )
        }),
        ('Nutritional Info', {
            'fields': ('calories', 'protein', 'carbs', 'fat'),
            'classes': ('collapse',),
        }),
    )

