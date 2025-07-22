from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.messages import get_messages

# Create your tests here.

class PasswordChangeTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='oldpass123')
        self.client.login(username='tester', password='oldpass123')

    def test_change_password_success(self):
        response = self.client.post(reverse('change_password'), {
            'old_password': 'oldpass123',
            'new_password1': 'newsecurepass456',
            'new_password2': 'newsecurepass456',
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('settings_view'))

        # Refresh user from DB and confirm new password works
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('newsecurepass456'))

        # Confirm success message
        messages = list(get_messages(response.wsgi_request))
        self.assertIn('✅ Password updated successfully.', [str(msg) for msg in messages])
