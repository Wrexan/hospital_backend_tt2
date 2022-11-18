from django.contrib.auth.models import AbstractUser, Group
from django.db import OperationalError


class User(AbstractUser):
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        try:
            client_group, _ = Group.objects.get_or_create(name='clients')
            self.groups.add(client_group)
        except OperationalError as err:
            print(err)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        default_permissions = ()

    def __str__(self):
        return self.username
