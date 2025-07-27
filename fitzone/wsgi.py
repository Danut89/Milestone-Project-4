"""
WSGI config for fitzone project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fitzone.settings')

application = get_wsgi_application()


# 🔧 Auto-run migrations on startup (for Render Free plan workaround)
import os
import django
from django.core.management import call_command

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fitzone.settings")
django.setup()
try:
    call_command("migrate", interactive=False)
except Exception as e:
    print(f"Migration failed: {e}")