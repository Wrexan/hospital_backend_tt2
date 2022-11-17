from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet
from .serializers import WorkerSerializer
from .models import Worker
from logic.views_logic import get_model_by_id_or_all


class WorkerViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    serializer_class = WorkerSerializer

    def get_queryset(self):
        return get_model_by_id_or_all(Worker, self.request)
