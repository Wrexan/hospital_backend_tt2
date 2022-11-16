from django.contrib.auth.models import AbstractUser, User


class Client(User):
    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.username
