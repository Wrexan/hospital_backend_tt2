from rest_framework.exceptions import PermissionDenied
from rest_framework.viewsets import ModelViewSet
from .serializers import WorkerSerializer
from .models import Worker
from logic.views_logic import get_model_by_id_or_all


class WorkerViewSet(ModelViewSet):
    serializer_class = WorkerSerializer

    def get_queryset(self):
        if self.request.user.has_perms([
            'workers.list_workers',
            'workers.view_worker',
            # 'worker.add_worker',
            # 'worker.change_worker',
            # 'worker.delete_worker',
        ]):
            # self.request.user.has_perm('worker.list_workers'):
            return get_model_by_id_or_all(Worker, self.request)
        raise PermissionDenied()
