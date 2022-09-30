from django.shortcuts import render
from rest_framework import status, viewsets
from housing.serializers import UserSerializer
from housing.models import User

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
