from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as token_views

from rest_framework_swagger.views import get_swagger_view

from . import views

router = DefaultRouter()
router.register(r'schedules', views.ScheduleViewSet)
router.register(r'lines', views.LineViewSet)
router.register(r'drivers', views.DriverViewSet)
router.register(r'trains', views.TrainViewSet)
router.register(r'stations', views.StationViewSet)
router.register(r'users', views.UserViewSet)

# Swagger
schema_view = get_swagger_view(title='TrainAPI')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'login/', include('rest_framework.urls')),
    url(r'token/', token_views.obtain_auth_token),
    url(r'^ratp/$', views.ratp_api_call),
    url(r'^swagger/$', schema_view)
]
