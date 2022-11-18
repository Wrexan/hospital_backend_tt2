from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        permissions = (
            ('list_workers', 'Can view list of workers'),
            ('view_schedules', 'Can view work hours of workers'),
        )

    def __str__(self):
        return self.username
