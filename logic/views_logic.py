def get_model_by_id_or_all(model, request):
    if 'id' in request.query_params:
        return model.objects.filter(pk=request.query_params.get('id'))
    return model.objects.all()