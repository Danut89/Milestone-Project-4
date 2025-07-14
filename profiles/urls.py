from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('settings/', views.settings_view, name='settings_view'),
    path('settings/edit-info/', views.edit_info_view, name='edit_info'),
    path('change-password/', views.change_password, name='change_password'),
    path('toggle-activity-visibility/', views.toggle_recent_activity_visibility, name='toggle_recent_activity'),
]
