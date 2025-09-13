from django.apps import AppConfig
import os

class FitzoneConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "fitzone"

    def ready(self):
        from django.db.models.signals import post_migrate
        from django.contrib.auth import get_user_model

        def create_admin(sender, **kwargs):
            """Create a default superuser if CREATE_SUPERUSER=1 is set."""
            if os.environ.get("CREATE_SUPERUSER") == "1":
                User = get_user_model()
                if not User.objects.filter(username="admin").exists():
                    User.objects.create_superuser(
                        username="admin",
                        email="admin@example.com",
                        password="Password123"
                    )
                    print("✅ Superuser created: admin / Password123")
                else:
                    print("⚠️ Superuser already exists")

        # Connect to post_migrate so it runs after migrations are applied
        post_migrate.connect(create_admin, sender=self)
