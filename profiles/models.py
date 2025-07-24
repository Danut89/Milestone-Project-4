from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """
    A user profile model for storing default delivery info and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    default_full_name = models.CharField(max_length=100, null=True, blank=True)
    default_email = models.EmailField(null=True, blank=True)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_address_line1 = models.CharField(max_length=255, null=True, blank=True)
    default_address_line2 = models.CharField(max_length=255, null=True, blank=True)
    default_city = models.CharField(max_length=100, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = models.CharField(max_length=100, null=True, blank=True)

    hide_recent_activity = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username