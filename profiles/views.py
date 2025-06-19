from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    return render(request, 'profiles/dashboard.html')

@login_required
def settings_view(request):
    return render(request, 'profiles/settings.html')
