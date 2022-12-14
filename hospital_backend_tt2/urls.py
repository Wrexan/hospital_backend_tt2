"""hospital_backend_tt2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from hospital.views import LocationViewSet, ScheduleViewSet, AppointmentViewSet
from users.views import UserViewSet
from workers.views import WorkerViewSet

router = DefaultRouter()
router.register('locations', LocationViewSet, basename='locations')
router.register('schedules', ScheduleViewSet, basename='schedules')
router.register('appointments', AppointmentViewSet, basename='appointments')
router.register('users', UserViewSet, basename='users')
router.register('workers', WorkerViewSet, basename='workers')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),
]
