from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Run migrations on Render DB without shell access'

    def handle(self, *args, **kwargs):
        self.stdout.write("Running migrations...")
        call_command('migrate')
        self.stdout.write(self.style.SUCCESS("Migrations applied successfully!"))
