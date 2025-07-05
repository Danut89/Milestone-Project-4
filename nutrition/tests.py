from django.test import TestCase
from django.contrib.auth.models import User
from .models import Recipe
from django.urls import reverse

# ✅ Recipe CRUD Tests using TDD for distinction-level functionality
class RecipeCRUDTests(TestCase):

    def setUp(self):
        # Set up a test user and log them in
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_create_recipe(self):
        response = self.client.post(reverse('nutrition:add_recipe'), {
            'title': 'Test Recipe',
            'ingredients': 'Test ingredients',
            'instructions': 'Test instructions',
            'prep_time_minutes': 15,
        })
        self.assertEqual(response.status_code, 302)  # Expect a redirect after creation
        self.assertEqual(Recipe.objects.count(), 1)
        self.assertEqual(Recipe.objects.first().title, 'Test Recipe')

    def test_update_recipe(self):
        # Create a recipe to update
        recipe = Recipe.objects.create(
            title='Old Title',
            ingredients='Old',
            instructions='Old',
            prep_time_minutes=10,
            author=self.user
        )
        response = self.client.post(reverse('nutrition:edit_recipe', args=[recipe.id]), {
            'title': 'New Title',
            'ingredients': 'Updated ingredients',
            'instructions': 'Updated instructions',
            'prep_time_minutes': 20,
        })
        self.assertEqual(response.status_code, 302)  # Expect a redirect
        recipe.refresh_from_db()
        self.assertEqual(recipe.title, 'New Title')

    def test_delete_recipe(self):
        # Create a recipe to delete
        recipe = Recipe.objects.create(
            title='To Delete',
            ingredients='Some',
            instructions='Delete me',
            prep_time_minutes=10,
            author=self.user
        )
        response = self.client.post(reverse('nutrition:delete_recipe', args=[recipe.id]))
        self.assertEqual(response.status_code, 302)  # Expect a redirect
        self.assertRedirects(response, reverse('nutrition:recipes'))  # ✅ Use correct name from urls.py
        self.assertEqual(Recipe.objects.count(), 0)
