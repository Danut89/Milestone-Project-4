from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from shop.models import Product
from nutrition.models import Recipe, MealPlan

# Create your tests here.
class GlobalSearchTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='pass')
        self.product = Product.objects.create(
            name='Search Product',
            description='desc',
            price=9.99,
            category='equipment',
        )
        self.recipe = Recipe.objects.create(
            title='Search Recipe',
            ingredients='i',
            instructions='i',
            prep_time_minutes=5,
            author=self.user,
        )
        self.meal_plan = MealPlan.objects.create(
            title='Search Plan',
            description='d',
            calories=100,
            duration_days=7,
            created_by=self.user,
        )

    def test_results_page_returned(self):
        response = self.client.get(reverse('global_search'), {'q': 'search'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/global_search_results.html')
        self.assertIn(self.product, response.context['products'])
        self.assertIn(self.recipe, response.context['recipes'])
        self.assertIn(self.meal_plan, response.context['meal_plans'])

    def test_no_results_redirects_with_message(self):
        response = self.client.get(
            reverse('global_search'),
            {'q': 'unknown'},
            HTTP_REFERER=reverse('home'),
        )
        self.assertRedirects(response, reverse('home'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'No results found.')