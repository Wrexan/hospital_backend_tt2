from django.contrib.auth.models import User


class Administrator(User):
    class Meta:
        verbose_name = 'Administrator'
        verbose_name_plural = 'Administrators'

    def __str__(self):
        return self.username


class Manager(User):
    class Meta:
        verbose_name = 'Manager'
        verbose_name_plural = 'Managers'

    def __str__(self):
        return self.username
