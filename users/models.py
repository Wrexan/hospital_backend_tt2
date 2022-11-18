from django.contrib.auth.models import AbstractUser, Group
from groups.models import clients


class User(AbstractUser):
    # groups = Group.objects.get(name='group 2')

    # clients_group = Group.objects.get(name='clients')
    # clients_group.user_set.add(self.request.user)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        # permissions = (
        #     ('list_workers', 'Can view list of workers'),
        #     ('view_schedules', 'Can view work hours of workers'),
        # )

    def __str__(self):
        return self.username
