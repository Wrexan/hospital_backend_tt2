from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.viewsets import ModelViewSet
from .serializers import LocationSerializer, ScheduleSerializer, AppointmentSerializer
from .models import Location, Schedule, Appointment
from logic.views_logic import get_model_by_id_or_all


class LocationViewSet(ModelViewSet):
    serializer_class = LocationSerializer

    # @action(detail=False)
    def get_queryset(self):
        if self.request.user.has_perms([
            'hospital.list_locations',
            'hospital.view_location',
            # 'location.add_location',
            # 'location.change_location',
            # 'location.delete_location',
        ]):
            return get_model_by_id_or_all(model=Location, request=self.request)
        raise PermissionDenied()

    @action(detail=True, methods=['post'])
    def add(self, request):
        if self.request.user.has_perm('hospital.add_location'):
            print(f'OK - hospital.add_location')
            serializer = self.serializer_class(self.request.query, many=True)
            if serializer.is_valid(raise_exception=True):
                Location.objects.create(self.request.query)
            #     print(f'OK - created')
            # return get_model_by_id_or_all(model=Location, request=self.request)
        raise PermissionDenied()


class ScheduleViewSet(ModelViewSet):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        if self.request.user.has_perms([
            'hospital.list_schedules',
            'hospital.view_schedule',
            # 'schedule.add_schedule',
            # 'schedule.change_schedule',
            # 'schedule.delete_schedule',
        ]):
            print(f'OK - schedule.list_schedules')
            return get_model_by_id_or_all(Schedule, self.request)
        raise PermissionDenied()


class AppointmentViewSet(ModelViewSet):
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        if self.request.user.has_perms([
            'hospital.list_appointments',
            'hospital.view_appointment',
            # 'hospital.add_schedule',
            # 'hospital.change_schedule',
            # 'hospital.delete_schedule',
        ]):
            print(f'OK - appointment.list_appointments')
            return get_model_by_id_or_all(Appointment, self.request)
        raise PermissionDenied()
