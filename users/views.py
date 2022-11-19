from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import UserSerializer
from logic.views_logic import permissions_only
from .models import User


class UserViewSet(ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    @permissions_only({'user.list_users'})
    def get_queryset(self):
        return User.objects.all()

    @permissions_only({'user.view_users'})
    def get_object(self, **kwargs):
        return User.objects.get(id=self.kwargs['pk'])

