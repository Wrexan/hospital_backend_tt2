from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet
from .serializers import ClientSerializer
from .models import Client
from logic.views_logic import get_model_by_id_or_all


class ClientViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    serializer_class = ClientSerializer

    def get_queryset(self):
        return get_model_by_id_or_all(Client, self.request)
