from django.shortcuts import render
from rest_framework import filters, viewsets, generics
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

class OwnerViewSet(generics.ListCreateAPIView):
    search_fields = ['contact_email', 'contact_number', 'id']
    filter_backends = (filters.SearchFilter,)
    queryset = models.Owner.objects.all()
    serializer_class = serializers.OwnerSerializer

class InterestedViewSet(viewsets.ModelViewSet):
    queryset = models.Interested.objects.all()
    serializer_class = serializers.InterestedSerializer

class LeaseViewSet(viewsets.ModelViewSet):
    queryset = models.Lease.objects.all()
    serializer_class = serializers.LeaseSerializer



class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = models.Apartment.objects.all()
    serializer_class = serializers.ApartmentSerializer

    