from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet

from hospital.serializers import LocationSerializer
from .models import Worker


class WorkerViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Worker.objects.all()
    serializer_class = LocationSerializer
