"""
    This is url file to add urls for respective models.
"""

from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import UserLogin, UserLogout

router = DefaultRouter()
router.register(r'flats', views.FlatViewSet, basename='flat')
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'leases', views.LeaseViewSet, basename='lease')
router.register(r'interests', views.InterestViewSet, basename='interest')
router.register(r'apartments', views.ApartmentViewSet, basename='apartment')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', UserLogin.as_view(), name='user_login'),
    path('logout/', UserLogout.as_view(), name='user_logout'),
    path('sign/<str:lease_identifier>/<str:username>/<str:dob>', views.sign_lease, name='sign_lease'),
    path('flats/<uuid:flat_id>/reviews/', views.ReviewListCreateView.as_view(), name='flat_reviews'),
]
'''Rest API endpoints'''