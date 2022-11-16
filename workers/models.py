from django.db import models


class Worker(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    speciality = models.CharField(max_length=64)
