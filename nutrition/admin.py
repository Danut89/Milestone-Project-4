from django.contrib import admin
from django.utils.html import format_html
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
    list_display = ('title', 'prep_time_minutes', 'calories', 'category', 'author', 'created_at', 'image_preview')
    search_fields = ('title', 'ingredients', 'instructions')
    list_filter = ('category', 'created_at', 'author')

    fieldsets = (
        (None, {
            'fields': (
                'title',
                'description',
                'category',
                'ingredients',
                'instructions',
                'prep_time_minutes',
                'image',
                'author',
            )
        }),
        ('Nutritional Info', {
            'fields': ('calories', 'protein', 'carbs', 'fat'),
            'classes': ('collapse',),
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 80px;" />', obj.image.url)
        return "No image"

    image_preview.short_description = "Preview"
