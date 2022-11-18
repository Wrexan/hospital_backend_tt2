from django.contrib.auth.decorators import login_required, permission_required
from rest_framework.exceptions import PermissionDenied
from rest_framework.viewsets import ModelViewSet
from .serializers import LocationSerializer, ScheduleSerializer, AppointmentSerializer
from .models import Location, Schedule, Appointment
from logic.views_logic import get_model_by_id_or_all


class LocationViewSet(ModelViewSet):
    serializer_class = LocationSerializer

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            raise PermissionDenied()
        if self.request.user.has_perms([
            'location.list_locations',
            'location.view_location',
            'location.add_location',
            'location.change_location',
            'location.delete_location',
        ]):
            return get_model_by_id_or_all(Location, self.request)
        raise PermissionDenied()


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
