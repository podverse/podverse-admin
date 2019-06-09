from django.apps import apps
from django.contrib.auth.management import create_permissions
from django.core.management import BaseCommand

class Command(BaseCommand):
    for app_config in apps.get_app_configs():
        app_config.models_module = True
        create_permissions(app_config, verbosity=0)
        app_config.models_module = None

    def handle(self, *args, **options):
        self.stdout.write("Permissions created.")
