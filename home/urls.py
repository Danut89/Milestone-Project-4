from django.urls import path
from .views import create_superuser_view

urlpatterns = [
    path('create-superuser/', create_superuser_view),
]
