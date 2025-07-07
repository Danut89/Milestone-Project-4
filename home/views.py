from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home/index.html')

@login_required
def dashboard(request):
    return render(request, 'home/dashboard.html')

