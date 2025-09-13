from django.urls import path
from home.views import run_migrations_view, collect_static_view

urlpatterns = [
    path('run-migrations/', run_migrations_view),
    path('collect-static/', collect_static_view),
]
