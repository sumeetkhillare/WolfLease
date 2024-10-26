# """
#     This is url file to add urls for respective models.
# """

# from django.urls import path, include
# from . import views
# from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# '''This is default Router'''


# urlpatterns = [
#     path('', include(router.urls)),
#     path('owners', views.OwnerViewSet.as_view()),
#     path('owners/<str:pk>', views.OwnerViewSet.as_view()),
#     path('flats', views.FlatViewSet.as_view()),
#     path('flats/<str:pk>', views.FlatViewSet.as_view()),
#     path('lease', views.LeaseViewSet.as_view()),
#     path('lease/<str:pk>', views.LeaseViewSet.as_view()),
#     path('interests', views.InterestedViewSet.as_view()),
#     path('interests/<str:pk>', views.InterestedViewSet.as_view()),
#     path('apartments', views.ApartmentViewSet.as_view()),
#     path('apartments/<str:pk>', views.ApartmentViewSet.as_view()),
#     path('users', views.UserViewSet.as_view()),
#     path('users/<str:pk>', views.UserViewSet.as_view()),
# ]
# '''Rest API endpoints'''



from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register your viewsets with it
router = DefaultRouter()
router.register(r'owners', views.OwnerViewSet)
router.register(r'flats', views.FlatViewSet)
router.register(r'leases', views.LeaseViewSet)
# router.register(r'interests', views.InterestedViewSet)
router.register(r'apartments', views.ApartmentViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/login/', views.CustomAuthToken.as_view(), name='login'),
]