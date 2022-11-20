from django.db.models import Q
from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Location, Schedule, Appointment


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class ScheduleSerializer(ModelSerializer):
    def validate(self, attrs):
        if attrs['time_start'] >= attrs['time_end']:
            raise ValidationError('Schedule cannot end before start')

        this_day_conflict_schedules = Schedule.objects \
            .filter(week_day=attrs['week_day']) \
            .filter(Q(time_start__lte=attrs['time_start']) & Q(time_end__gte=attrs['time_start']) |
                    Q(time_start__lte=attrs['time_end']) & Q(time_end__gte=attrs['time_end']))

        location_schedules = this_day_conflict_schedules.filter(location=attrs['location'])
        if location_schedules.exists():
            busy_location_name = location_schedules.first().location.name
            busy_location_time = ', '.join(f'{_time.time_start} {_time.time_end}'
                                           for _time in location_schedules.order_by('time_start'))
            raise ValidationError(f'Location {busy_location_name} is busy for: {busy_location_time}')

        worker_schedules = this_day_conflict_schedules.filter(worker=attrs['worker'])
        if worker_schedules.exists():
            busy_worker_name = worker_schedules.first().worker.name
            busy_worker_time = ', '.join(f'{_time.time_start} {_time.time_end}'
                                         for _time in worker_schedules.order_by('time_start'))
            raise ValidationError(f'Worker {busy_worker_name} is busy for: {busy_worker_time}')

    class Meta:
        model = Schedule
        fields = '__all__'


class AppointmentSerializer(ModelSerializer):
    def validate(self, attrs):
        if attrs['time_start'] >= attrs['time_end']:
            raise ValidationError('Appointment cannot end before start')

        week_day = attrs['date'].isoweekday()
        this_day_suitable_schedule = Schedule.objects \
            .filter(week_day=week_day) \
            .filter(worker=attrs['worker']) \
            .filter(Q(time_start__lte=attrs['time_start']) & Q(time_end__gte=attrs['time_end']))
        if not this_day_suitable_schedule.exists():
            raise ValidationError(f"Not proper working time for {attrs['worker']}")

        this_date_conflicting_appointments = Appointment.objects \
            .filter(date=attrs['date']) \
            .filter(worker=attrs['worker']) \
            .filter(Q(time_start__lte=attrs['time_start']) & Q(time_end__gte=attrs['time_start']) |
                    Q(time_start__lte=attrs['time_end']) & Q(time_end__gte=attrs['time_end']))
        if this_date_conflicting_appointments.exists():
            busy_worker_time = ', '.join(f'{_time.time_start} {_time.time_end}'
                                         for _time in this_date_conflicting_appointments.order_by('time_start'))
            raise ValidationError(f"Worker {attrs['worker']} is busy for: {busy_worker_time}")
        return attrs

    class Meta:
        model = Appointment
        fields = '__all__'
