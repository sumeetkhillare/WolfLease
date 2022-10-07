from django.shortcuts import render
from rest_framework import status, viewsets
from housing import serializers
from housing import models


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

class FlatViewSet(viewsets.ModelViewSet):
    queryset = models.Flat.objects.all()
    serializer_class = serializers.FlatSerializer

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = models.Owner.objects.all()
    serializer_class = serializers.OwnerSerializer

class InterestedViewSet(viewsets.ModelViewSet):
    queryset = models.Interested.objects.all()
    serializer_class = serializers.InterestedSerializer

class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = models.Apartment.objects.all()
    serializer_class = serializers.ApartmentSerializer

