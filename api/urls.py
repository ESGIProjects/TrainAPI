from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as token_views

from . import views

router = DefaultRouter()
router.register(r'schedules', views.ScheduleViewSet)
router.register(r'lines', views.LineViewSet)
router.register(r'drivers', views.DriverViewSet)
router.register(r'trains', views.TrainViewSet)
router.register(r'stations', views.StationViewSet)
router.register(r'users', views.UserViewSet)

# Login and logout views for the browsable API
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'login/', include('rest_framework.urls')),
    url(r'token/', token_views.obtain_auth_token)
]
