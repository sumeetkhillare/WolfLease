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
    # path('owners', views.OwnerViewSet.as_view()),
    # path('owners/<str:pk>', views.OwnerViewSet.as_view()),
    # path('flats', views.FlatViewSet.as_view()),
    # path('flats/<str:pk>', views.FlatViewSet.as_view()),
    # path('lease', views.LeaseViewSet.as_view()),
    # path('lease/<str:pk>', views.LeaseViewSet.as_view()),
    # path('interests', views.InterestedViewSet.as_view()),
    # path('interests/<str:pk>', views.InterestedViewSet.as_view()),
    # path('apartments', views.ApartmentViewSet.as_view()),
    # path('apartments/<str:pk>', views.ApartmentViewSet.as_view()),
    # path('users', views.UserViewSet.as_view()),
    # path('users/<str:pk>', views.UserViewSet.as_view()),
    path('login/', UserLogin.as_view(), name='user_login'),
    path('logout/', UserLogout.as_view(), name='user_logout'),
    path('sign/<str:lease_identifier>/<str:username>/<str:dob>', views.sign_lease, name='sign_lease'),
]
'''Rest API endpoints'''
