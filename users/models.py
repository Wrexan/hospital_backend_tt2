from django.contrib.auth.models import AbstractUser, Group


class User(AbstractUser):
    groups = Group.objects.get(name='clients')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username
