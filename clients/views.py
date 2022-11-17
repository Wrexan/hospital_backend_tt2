from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet

from hospital.serializers import LocationSerializer
from .models import Client


class ClientViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Client.objects.all()
    serializer_class = LocationSerializer
