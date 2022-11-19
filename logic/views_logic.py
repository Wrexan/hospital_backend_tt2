from rest_framework.exceptions import PermissionDenied, NotFound


def get_model_by_id_or_all(model, request, is_auth=True):
    if is_auth and not request.user.is_authenticated:
        raise PermissionDenied()
    if 'pk' in request.query_params:
        # print(f'OK - {model._meta.verbose_name.title()}.view_{model._meta.verbose_name.title()}')
        return model.objects.filter(pk=request.query_params.get('pk'))
    # print(f'OK - {model._meta.verbose_name.title()}.list_{model._meta.verbose_name.title()}s')
    return model.objects.all()


def get_self_user_info(model, request):
    if not request.user.is_authenticated:
        raise PermissionDenied()
    if request.user.pk:
        return model.objects.filter(pk=request.user.pk)
