from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import UserSerializer
from logic.views_logic import get_model_by_id_or_all, get_self_user_info
from .models import User


class UserViewSet(ReadOnlyModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.user.has_perm('user.list_users'):
            return get_model_by_id_or_all(User, self.request)
        return get_self_user_info(User, self.request)

