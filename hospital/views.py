from django.http import Http404, HttpResponseRedirect
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.exceptions import PermissionDenied, NotFound
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import LocationSerializer, ScheduleSerializer, AppointmentSerializer
from .models import Location, Schedule, Appointment
from logic.views_logic import get_model_by_id_or_all


class LocationViewSet(ModelViewSet):
    serializer_class = LocationSerializer
    permission_classes = (IsAuthenticated,)

    # @action(detail=False)
    def get_queryset(self):
        if self.request.user.has_perm('hospital.list_locations'):
            return Location.objects.all()
        raise PermissionDenied()

    def get_object(self, **kwargs):
        if self.request.user.has_perm('hospital.view_location'):
            return Location.objects.get(id=self.kwargs['pk'])
        raise PermissionDenied()

    def create(self, request, *args, **kwargs):
        if self.request.user.has_perm('hospital.add_location'):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        raise PermissionDenied()

    def partial_update(self, request, *args, **kwargs):
        if self.request.user.has_perm('hospital.change_location'):
            kwargs['partial'] = True
            return self.update(request, *args, **kwargs)
        raise PermissionDenied()

    def destroy(self, request, *args, **kwargs):
        if self.request.user.has_perm('hospital.delete_location'):
            try:
                instance = self.get_object()
                self.perform_destroy(instance)
            except Http404:
                pass
            raise NotFound()
        raise PermissionDenied()


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
