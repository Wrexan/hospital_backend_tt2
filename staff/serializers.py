from rest_framework.serializers import ModelSerializer
from .models import Administrator, Manager


class AdministratorSerializer(ModelSerializer):
    class Meta:
        model = Administrator
        fields = '__all__'


class ManagerSerializer(ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'
