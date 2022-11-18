from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management import BaseCommand

from hospital.models import Location, Schedule, Appointment
from users.models import User

from workers.models import Worker

clients = {
    'name': 'clients',
    'permissions': (
        'worker.list_workers',
        'worker.view_workers',

        'schedule.list_schedules',
        'schedule.view_schedule',
    )
}

admins = {
    'name': 'admins',
    'permissions': {
        Worker: ('worker.list_workers', 'worker.view_worker'),
        User: ('user.list_users', 'user.view_user',),
        Appointment: ('list_appointments', 'view_appointment', 'add_appointment'
                      , 'change_appointment', 'delete_appointment')
    }
}

managers = {
    'name': 'managers',
    'permissions': {
        Worker: ('list_workers', 'view_worker', 'add_worker', 'change_worker', 'delete_worker'),
        Schedule: ('list_schedules', 'view_schedule', 'add_schedule', 'change_schedule', 'delete_schedule'),
        Location: ('list_locations', 'view_location', 'add_location', 'change_location', 'delete_location')
    }
}


class Command(BaseCommand):
    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name='managers')
        content_type = ContentType.objects.get_for_model(Location)
        permission, _ = Permission.objects.get_or_create(codename='view_location',
                                                         name='Can view Location',
                                                         content_type=content_type)
        # permission = Permission.objects.create(codename='view_location',
        #                                        name='Can view Location',
        #                                        content_type=content_type)
        group.permissions.add(permission)
        group.save()
        # super_user = User.objects.create_superuser('admin', '', 'admin')
        # super_user.save()
        print(f"Group managers created.")
