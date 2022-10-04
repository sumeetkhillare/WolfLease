from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'users', views.UserViewSet, basename="user_viewset")
router.register(r'flats', views.FlatViewSet, basename="flat_viewset")

urlpatterns = [
    path('', include(router.urls)),
]