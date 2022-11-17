from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer
from logic.views_logic import get_model_by_id_or_all
from .models import User


class UserViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    serializer_class = UserSerializer

    def get_queryset(self):
        return get_model_by_id_or_all(User, self.request)
