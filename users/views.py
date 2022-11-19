from django.db.models import Q
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import UserSerializer
from logic.views_logic import permissions_only
from .models import User


class UserViewSet(ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    @permissions_only({'users.list_users'})
    def get_queryset(self):
        return User.objects.all().exclude(is_superuser=True)

    @permissions_only({'users.view_users'})
    def get_object(self, **kwargs):
        user = get_object_or_404(User, ~Q(is_superuser=True), id=self.kwargs['pk'])

