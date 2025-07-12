from django import forms

class CheckoutForm(forms.Form):
    full_name = forms.CharField(
        max_length=100,
        required=True,
        label="Full Name",
        widget=forms.TextInput(attrs={
            'placeholder': 'e.g. Danut Grigore',
        })
    )

    email = forms.EmailField(
        required=True,
        label="Email Address",
        widget=forms.EmailInput(attrs={
            'placeholder': 'e.g. you@example.com',
        })
    )

    phone_number = forms.CharField(
        max_length=20,
        required=True,
        label="Phone Number",
        widget=forms.TextInput(attrs={
            'placeholder': 'e.g. 07712345678',
        })
    )

    address_line1 = forms.CharField(
        max_length=255,
        required=True,
        label="Address Line 1",
        widget=forms.TextInput(attrs={
            'placeholder': 'Street address or P.O. Box',
        })
    )

    address_line2 = forms.CharField(
        max_length=255,
        required=False,
        label="Address Line 2",
        widget=forms.TextInput(attrs={
            'placeholder': 'Apartment, suite, unit etc. (optional)',
        })
    )

    city = forms.CharField(
        max_length=100,
        required=True,
        label="City",
        widget=forms.TextInput(attrs={
            'placeholder': 'e.g. Hull',
        })
    )

    postcode = forms.CharField(
        max_length=20,
        required=True,
        label="Postcode",
        widget=forms.TextInput(attrs={
            'placeholder': 'e.g. HU5 3BT',
        })
    )

    country = forms.CharField(
        max_length=100,
        required=True,
        label="Country",
        widget=forms.TextInput(attrs={
            'placeholder': 'e.g. United Kingdom',
        })
    )


