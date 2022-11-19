from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q

from workers.models import Worker
from users.models import User


class Location(models.Model):
    name = models.CharField(max_length=64, unique=True)

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
    time_start = models.TimeField('Schedule start time: HH:MM', auto_now=False, default='08:00')
    time_end = models.TimeField('Schedule end time: HH:MM', auto_now=False, default='12:00')

    def clean(self):
        if self.time_start >= self.time_end:
            raise ValidationError('Schedule cannot end before start')

        day_schedules = Schedule.objects \
            .filter(week_day=self.week_day) \
            .filter(Q(time_start__lte=self.time_start) & Q(time_end__gte=self.time_start) |
                    Q(time_start__lte=self.time_end) & Q(time_end__gte=self.time_end))

        location_schedules = day_schedules.filter(location=self.location)
        if location_schedules.exists():
            busy_location_name = location_schedules.first().location.name
            busy_location_time = ', '.join(f'{_time.time_start} {_time.time_end}'
                                           for _time in location_schedules.order_by('time_start'))
            raise ValidationError(f'Location {busy_location_name} is busy for: {busy_location_time}')

        worker_schedules = day_schedules.filter(worker=self.worker)
        if worker_schedules.exists():
            busy_worker_name = worker_schedules.first().worker.name
            busy_worker_time = ', '.join(f'{_time.time_start} {_time.time_end}'
                                         for _time in worker_schedules.order_by('time_start'))
            raise ValidationError(f'Worker {busy_worker_name} is busy for: {busy_worker_time}')

    class Meta:
        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedules'

    def __str__(self):
        return f'[{self.worker.speciality}] {self.worker.first_name} {self.worker.last_name} => ' \
               f'{self.WEEK_DAYS[self.week_day - 1][1]}: ' \
               f'{self.time_start}-{self.time_end}'


class Appointment(models.Model):
    name = models.CharField(max_length=64)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    worker = models.ForeignKey(to=Worker, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False)
    time_start = models.TimeField(auto_now=False)
    time_end = models.TimeField(auto_now=False)

    class Meta:
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'
