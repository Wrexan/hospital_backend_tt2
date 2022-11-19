from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from hospital.models import Schedule
from .models import Worker


class WorkerSerializer(ModelSerializer):
    week_day = None

    schedule_times = SerializerMethodField()

    class Meta:
        model = Worker
        fields = '__all__'

    def get_schedule_times(self, obj):
        if not self.week_day:
            # self.Meta.fields = ['first_name', 'last_name', 'speciality']
            return None
        return Schedule.objects \
            .filter(worker_id=obj.pk,
                    week_day=self.week_day) \
            .order_by('time_start').values('location__name', 'time_start', 'time_end')
