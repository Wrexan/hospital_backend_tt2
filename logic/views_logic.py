from rest_framework.exceptions import PermissionDenied


def get_model_by_id_or_all(model, request, is_auth=True):
    if is_auth and not request.user.is_authenticated:
        raise PermissionDenied()
    if 'id' in request.query_params:
        return model.objects.filter(pk=request.query_params.get('id'))
    return model.objects.all()


def get_self_user_info(model, request):
    if not request.user.is_authenticated:
        raise PermissionDenied()
    if request.user.pk:
        return model.objects.filter(pk=request.user.pk)
