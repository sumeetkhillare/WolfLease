from django.shortcuts import render
from rest_framework import status, viewsets
from housing.serializers import FlatSerializer, UserSerializer
from housing.models import User
from .models import Flat

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FlatViewSet(viewsets.ModelViewSet):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer
    
