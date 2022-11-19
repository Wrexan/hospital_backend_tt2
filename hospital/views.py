from django.http import Http404
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import LocationSerializer, ScheduleSerializer, AppointmentSerializer
from .models import Location, Schedule, Appointment
from logic.views_logic import permissions_only


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

    @permissions_only({'hospital.list_schedules'})
    def get_queryset(self):
        return Schedule.objects.all()

    @permissions_only({'hospital.view_schedule'})
    def get_object(self, **kwargs):
        return Schedule.objects.get(id=self.kwargs['pk'])

    @permissions_only({'hospital.add_schedule'})
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @permissions_only({'hospital.change_schedule'})
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    @permissions_only({'hospital.delete_schedule'})
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        raise NotFound()


class AppointmentViewSet(ModelViewSet):
    serializer_class = AppointmentSerializer
    permission_classes = (IsAuthenticated,)

    @permissions_only({'hospital.list_appointments'})
    def get_queryset(self):
        return Appointment.objects.all()

    @permissions_only({'hospital.view_appointment'})
    def get_object(self, **kwargs):
        return Appointment.objects.get(id=self.kwargs['pk'])

    @permissions_only({'hospital.add_appointment'})
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @permissions_only({'hospital.change_appointment'})
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    @permissions_only({'hospital.delete_appointment'})
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        raise NotFound()
