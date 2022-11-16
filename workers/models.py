from django.db import models


class Worker(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    speciality = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Worker'
        verbose_name_plural = 'Workers'

    def __str__(self):
        return f'{self.speciality}: {self.first_name} {self.last_name}'
