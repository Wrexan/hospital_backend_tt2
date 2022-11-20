from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        super_user = User.objects.create_superuser('admin', '', 'admin')
        super_user.save()
        print("Superuser created. USERNAME: 'admin' PASSWORD: 'admin'")

        manager = User.objects.create_user('manager', '', '123')
        manager_group = Group.objects.get(name='managers')
        manager.save()
        manager_group.user_set.add(manager)
        print("Manager created. USERNAME: 'manager' PASSWORD: '123'")

        administrator = User.objects.create_user('administrator', '', '123')
        administrator_group = Group.objects.get(name='admins')
        administrator.save()
        administrator_group.user_set.add(administrator)
        print("Administrator created. USERNAME: 'administrator' PASSWORD: '123'")
