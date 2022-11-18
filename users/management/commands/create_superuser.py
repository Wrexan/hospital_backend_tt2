from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        super_user = User.objects.create_superuser('admin', '', 'admin')
        super_user.save()
        print("Superuser created. USERNAME: 'admin' PASSWORD: 'admin'")
