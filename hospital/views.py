from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet
from .serializers import LocationSerializer, ScheduleSerializer, AppointmentSerializer
from .models import Location, Schedule, Appointment
from logic.views_logic import get_model_by_id_or_all


class LocationViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    serializer_class = LocationSerializer

    def get_queryset(self):
        return get_model_by_id_or_all(Location, self.request)


class ScheduleViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        return get_model_by_id_or_all(Schedule, self.request)


class AppointmentViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        return get_model_by_id_or_all(Appointment, self.request)

