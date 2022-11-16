from rest_framework.serializers import ModelSerializer
from .models import Location, Schedule, Appointment


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class ScheduleSerializer(ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class AppointmentSerializer(ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
