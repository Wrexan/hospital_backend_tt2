from django.contrib.auth.decorators import login_required, permission_required
from rest_framework.viewsets import ModelViewSet
from .serializers import LocationSerializer, ScheduleSerializer, AppointmentSerializer
from .models import Location, Schedule, Appointment
from logic.views_logic import get_model_by_id_or_all


class LocationViewSet(ModelViewSet):
    serializer_class = LocationSerializer

    @login_required
    @permission_required('location.view_location')
    def get_queryset(self):
        return get_model_by_id_or_all(Location, self.request)


class ScheduleViewSet(ModelViewSet):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return get_model_by_id_or_all(Schedule, self.request)


class AppointmentViewSet(ModelViewSet):
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return get_model_by_id_or_all(Appointment, self.request)
