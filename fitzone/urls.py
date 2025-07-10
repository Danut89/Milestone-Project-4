"""
URL configuration for fitzone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home import views as home_views
from django.conf import settings
from django.conf.urls.static import static
from nutrition.views import meal_plan_detail




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.home, name='home'),
    path('accounts/', include('allauth.urls')),
    path('dashboard/', home_views.dashboard, name='dashboard'),
    path('contact/', home_views.contact_view, name='contact'),
    path('workouts/', include('workouts.urls')),
    path('profile/', include('profiles.urls')),
    path('nutrition/', include('nutrition.urls')),
    path('shop/', include('shop.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)