from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()

router.register(r'users', views.UserViewSet, basename="user_viewset")
router.register(r'flats', views.FlatViewSet, basename="flat_viewset")
router.register(r'owners', views.OwnerViewSet, basename="owner_viewset")
router.register(r'interests', views.InterestedViewSet, basename="interests_viewset")
router.register(r'apartments', views.ApartmentViewSet, basename="apartment_viewset")
router.register(r'lease', views.LeaseViewSet, basename='lease_viewset')

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]