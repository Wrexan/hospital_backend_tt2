from django.http import Http404
from rest_framework import status
from rest_framework.exceptions import PermissionDenied, NotFound
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import LocationSerializer, ScheduleSerializer, AppointmentSerializer
from .models import Location, Schedule, Appointment
from logic.views_logic import permissions_only, get_model_by_id_or_all


class LocationViewSet(ModelViewSet):
    serializer_class = LocationSerializer
    permission_classes = (IsAuthenticated,)

    @permissions_only({'hospital.list_locations'})
    def get_queryset(self):
        return Location.objects.all()

    @permissions_only({'hospital.view_location'})
    def get_object(self, **kwargs):
        return Location.objects.get(id=self.kwargs['pk'])

    @permissions_only({'hospital.add_location'})
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @permissions_only({'hospital.change_location'})
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    @permissions_only({'hospital.delete_location'})
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        raise NotFound()


class ScheduleViewSet(ModelViewSet):
    serializer_class = ScheduleSerializer
    permission_classes = (IsAuthenticated,)

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
    permission_classes = (IsAuthenticated,)

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
