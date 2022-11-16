from django.contrib import admin
from .models import Location, Schedule, Appointment


admin.site.register(Location)
admin.site.register(Schedule)
admin.site.register(Appointment)
