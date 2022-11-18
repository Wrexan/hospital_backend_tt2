from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management import BaseCommand

from hospital.models import Location, Schedule, Appointment
from users.models import User

from workers.models import Worker

groups = (
    {
        'name': 'clients',
        'permissions': {
            Worker: ('list_workers', 'view_worker'),
            Schedule: ('list_schedules', 'view_schedule')
        },
    }, {
        'name': 'admins',
        'permissions': {
            Worker: ('list_workers', 'view_worker'),
            User: ('list_users', 'view_user',),
            Appointment: ('list_appointments', 'view_appointment', 'add_appointment',
                          'change_appointment', 'delete_appointment')
        }
    }, {
        'name': 'managers',
        'permissions': {
            Worker: ('list_workers', 'view_worker', 'add_worker', 'change_worker', 'delete_worker'),
            Schedule: ('list_schedules', 'view_schedule', 'add_schedule', 'change_schedule', 'delete_schedule'),
            Location: ('list_locations', 'view_location', 'add_location', 'change_location', 'delete_location')
        }
    }
)


class Command(BaseCommand):
    def handle(self, *args, **options):
        permissions = Permission.objects.all()
        for group in groups:
            new_group, created = Group.objects.get_or_create(name=group['name'])
            for model, permission_pack in group['permissions'].items():
                try:
                    content_type = ContentType.objects.get_for_model(model)
                    for codename in permission_pack:
                        permission = permissions.filter(codename=codename).first()
                        if not permission:
                            permission, _ = Permission.objects.get_or_create(codename=codename,
                                                                             name=f'Can {codename.replace("_", " ")}',
                                                                             content_type=content_type)
                        new_group.permissions.add(permission)
                        new_group.save()
                except Exception as err:
                    print(f"Error: {codename=} Can {codename.replace('_', ' ')}")
                    print(f"Error while creating a group: {err}")
            print(f"Created group: {group['name']}")
