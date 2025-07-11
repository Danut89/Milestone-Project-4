from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('settings/', views.settings_view, name='settings_view'),
    path('settings/edit-info/', views.edit_info_view, name='edit_info'),
]
