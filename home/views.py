from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home/index.html')

@login_required
def dashboard(request):
    return render(request, 'home/dashboard.html')

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # You could save this info or send an email
        messages.success(request, "Thanks for contacting us! We'll get back to you soon.")
        return redirect('contact')

    return render(request, 'home/contact.html')
