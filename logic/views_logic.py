def get_model_by_id_or_all(model, request):
    if 'id' in request.query_params:
        return model.objects.filter(pk=request.query_params.get('id'))
    return model.objects.all()


def get_self_user_info(model, request):
    if request.user.pk:
        return model.objects.filter(pk=request.user.pk)
