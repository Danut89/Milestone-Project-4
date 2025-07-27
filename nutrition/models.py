from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class MealPlan(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    calories = models.IntegerField()
    duration_days = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='mealplan_images/', blank=True, null=True)

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=1,
        limit_choices_to={'is_staff': True}
    )

    def __str__(self):
        return self.title

    @property
    def get_days(self):
        return self.days.all()


class MealPlanDay(models.Model):
    meal_plan = models.ForeignKey(MealPlan, on_delete=models.CASCADE, related_name="days")
    day_number = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    meals = models.TextField(blank=True, null=True)  # Optional: simple text for meals

    class Meta:
        ordering = ['day_number']

    def __str__(self):
        return f"{self.meal_plan.title} - Day {self.day_number}"



# ✅ Predefined categories for recipes
RECIPE_CATEGORIES = [
    ('breakfast', 'Breakfast'),
    ('lunch', 'Lunch'),
    ('dinner', 'Dinner'),
    ('snack', 'Snack'),
    ('dessert', 'Dessert'),
    ('vegan', 'Vegan'),
    ('keto', 'Keto'),
]

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    prep_time_minutes = models.IntegerField()
    image = CloudinaryField('image', blank=True, null=True)
    description = models.TextField(blank=True, null=True, help_text="Short description or context about the recipe.")
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=1,
        related_name="recipes"
    )

    # ✅ Nutritional info
    calories = models.PositiveIntegerField(blank=True, null=True)
    protein = models.CharField(max_length=20, blank=True, null=True)
    carbs = models.CharField(max_length=20, blank=True, null=True)
    fat = models.CharField(max_length=20, blank=True, null=True)

    # ✅ New category field
    category = models.CharField(
        max_length=20,
        choices=RECIPE_CATEGORIES,
        default='lunch',
        blank=True,
        null=True,
        help_text="Classify the recipe to improve filtering and UX."
    )

    def __str__(self):
        return self.title







class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlist')
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, null=True, blank=True, related_name='wishlisted_by')
    meal_plan = models.ForeignKey('MealPlan', on_delete=models.CASCADE, null=True, blank=True, related_name='wishlisted_by')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'recipe'], name='unique_user_recipe_wishlist'),
            models.UniqueConstraint(fields=['user', 'meal_plan'], name='unique_user_mealplan_wishlist'),
        ]

    def __str__(self):
        if self.recipe:
            return f"{self.user.username} → Recipe: {self.recipe.title}"
        elif self.meal_plan:
            return f"{self.user.username} → Meal Plan: {self.meal_plan.title}"
        return f"{self.user.username} → Wishlist item"
