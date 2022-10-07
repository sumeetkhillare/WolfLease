from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'users', views.UserViewSet, basename="user_viewset")
# router.register(r'flats', views.FlatViewSet, basename="flat_viewset")
# router.register(r'owners', views.OwnerViewSet, basename="owner_viewset")
router.register(r'interests', views.InterestedViewSet, basename="interests_viewset")
router.register(r'apartments', views.ApartmentViewSet, basename="apartment_viewset")
router.register(r'lease', views.LeaseViewSet, basename='lease_viewset')

urlpatterns = [
    path('', include(router.urls)),
    path('owners', views.OwnerViewSet.as_view()),
    path('owners/<str:pk>', views.OwnerViewSet.as_view()),
    path('flats', views.FlatViewSet.as_view()),
    path('flats/<str:pk>', views.FlatViewSet.as_view()),
]