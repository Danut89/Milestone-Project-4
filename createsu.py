from django.contrib.auth import get_user_model

def run():
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
