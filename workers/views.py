from datetime import datetime

from django.http import Http404
from django.utils.dateparse import parse_date
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from hospital.serializers import ScheduleSerializer
from .serializers import WorkerSerializer
from .models import Worker
from hospital.models import Schedule
from logic.views_logic import permissions_only


class WorkerViewSet(ModelViewSet):
    serializer_class = WorkerSerializer
    permission_classes = (IsAuthenticated,)

    @permissions_only({'workers.list_workers'})
    def get_queryset(self):
        if 'speciality' in self.request.query_params:
            return Worker.objects\
                .filter(speciality=self.request.query_params.get('speciality'))\
                .order_by('first_name')
        return Worker.objects.all().order_by('first_name')

    @permissions_only({'workers.view_worker'})
    def get_object(self, **kwargs):
        if 'date' in self.request.query_params:
            date = parse_date(self.request.query_params.get('date'))
            week_day = datetime.isoweekday(date)
            self.serializer_class.week_day = week_day
            return Worker.objects.get(id=self.kwargs['pk'])
        return Worker.objects.get(id=self.kwargs['pk'])

    @permissions_only({'workers.add_worker'})
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @permissions_only({'workers.change_worker'})
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    @permissions_only({'workers.delete_worker'})
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        raise NotFound()
