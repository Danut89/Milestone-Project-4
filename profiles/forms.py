from django import forms
from django.contrib.auth.models import User

class UserUpdateForm(forms.ModelForm):
    """Form to update user's name and email"""

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }

from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    """Form to update user profile delivery info"""
    class Meta:
        model = UserProfile
        fields = [
            'default_full_name', 'default_email', 'default_phone_number',
            'default_address_line1', 'default_address_line2',
            'default_city', 'default_postcode', 'default_country',
        ]
        widgets = {
            'default_full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'default_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'default_phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'default_address_line1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address Line 1'}),
            'default_address_line2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address Line 2'}),
            'default_city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'default_postcode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Postcode'}),
            'default_country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}),
        }
