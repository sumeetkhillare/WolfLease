from django.shortcuts import render
from rest_framework import status, viewsets
from housing.serializers import FlatSerializer, UserSerializer
from housing import models


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = models.User.objects.all()
    serializer_class = UserSerializer

class FlatViewSet(viewsets.ModelViewSet):
    queryset = models.Flat.objects.all()
    serializer_class = FlatSerializer

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = models.Owner.objects.all()
    serializer_class = OwnerSerializer

