from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet

from hospital.serializers import LocationSerializer
from .models import Administrator, Manager


class AdministratorViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Administrator.objects.all()
    serializer_class = LocationSerializer


class ManagerViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Manager.objects.all()
    serializer_class = LocationSerializer
