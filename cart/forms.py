from django import forms

class CheckoutForm(forms.Form):
    full_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=20, required=True)
    address_line1 = forms.CharField(max_length=255, required=True)
    address_line2 = forms.CharField(max_length=255, required=False)
    city = forms.CharField(max_length=100, required=True)
    postcode = forms.CharField(max_length=20, required=True)
    country = forms.CharField(max_length=100, required=True)

