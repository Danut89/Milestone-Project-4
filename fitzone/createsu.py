from django.core.management import call_command

def run():
    try:
        call_command(
            "createsuperuser",
            interactive=False,
            username="admin",
            email="admin@example.com",
            skip_checks=True
        )
    except Exception as e:
        print(f"⚠️ Could not auto-create superuser: {e}")

