from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from users.models import User

staff = (
    {
        'name': 'Superuser',
        'username': 'admin',
        'password': 'admin',
        'group': '',
        'superuser': True
    },
    {
        'name': 'Manager',
        'username': 'manager',
        'password': '123',
        'group': 'managers',
        'superuser': False
    },
    {
        'name': 'Administrator',
        'username': 'administrator',
        'password': '123',
        'group': 'admins',
        'superuser': False
    },
    {
        'name': 'Client',
        'username': 'client',
        'password': '123',
        'group': 'clients',
        'superuser': False
    },
)


class Command(BaseCommand):
    def handle(self, *args, **options):
        for user_data in staff:
            user_exist = User.objects.filter(username=user_data['username'])
            if user_exist.exists():
                continue
            if user_data['superuser']:
                user = User.objects.create_superuser(user_data['username'], '', user_data['password'])
                user.save()
            else:
                user = User.objects.create_user(user_data['username'], '', user_data['password'])
                user.save()
                user_group = Group.objects.get(name=user_data['group'])
                user_group.user_set.add(user)
            print(f"{user_data['name']} created. USERNAME: {user_data['username']} PASSWORD: {user_data['password']}")
