from django.core.exceptions import ValidationError
from django.db import models
from workers.models import Worker
from clients.models import Client


class Location(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

    def __str__(self):
        return self.name


class Schedule(models.Model):
    WEEK_DAYS = [
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
        (6, 'Saturday'),
        (7, 'Sunday'),
    ]
    worker = models.ForeignKey(to=Worker, on_delete=models.CASCADE)
    location = models.ForeignKey(to=Location, on_delete=models.CASCADE)
    week_day = models.PositiveSmallIntegerField(choices=WEEK_DAYS)
    time_start = models.TimeField(auto_now=False)
    time_end = models.TimeField(auto_now=False)

    def clean(self):
        if self.time_start >= self.time_end:
            raise ValidationError('Time cannot be reversed')

    class Meta:
        verbose_name = 'Working hours'
        verbose_name_plural = 'Working hours'

    def __str__(self):
        return f'{self.week_day}: {self.time_start}-{self.time_end}'


class Appointment(models.Model):
    name = models.CharField(max_length=64)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    worker = models.ForeignKey(to=Worker, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False)
    time_start = models.TimeField(auto_now=False)
    time_end = models.TimeField(auto_now=False)
