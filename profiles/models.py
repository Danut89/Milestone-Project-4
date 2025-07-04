from django.conf import settings
from nutrition.models import Recipe
from django.db import models

# Create your models here.

class RecipeWishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='saved_recipes')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_wishlist_entries')
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'recipe')
        ordering = ['-saved_at']

    def __str__(self):
        return f"{self.user} saved {self.recipe.title}"
