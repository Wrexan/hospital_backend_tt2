from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet
from .serializers import LocationSerializer, ScheduleSerializer, AppointmentSerializer
from .models import Location, Schedule, Appointment


class LocationViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class ScheduleViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class AppointmentViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
