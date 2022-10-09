from django.shortcuts import render
from rest_framework import filters, viewsets, generics
from housing import serializers
from housing import models
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

"""
    This is a file to add views for models. 
"""
# Create your views here.
class UserViewSet(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    """
    This viewset automatically provides CRUD actions for User model.
    """

# Add search fields to the user view set
    search_fields = ['contact_email', 'contact_number']
    filter_backends = (filters.SearchFilter,)
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

class FlatViewSet(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    """
    This viewset automatically provides CRUD actions for Flat model.
    """
    search_fields = ['availability', 'rent_per_room']
    filter_backends = (filters.SearchFilter,)
    queryset = models.Flat.objects.all()
    serializer_class = serializers.FlatSerializer

class OwnerViewSet(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    """
    This viewset automatically provides CRUD actions for Owner model.
    """
    search_fields = ['contact_email', 'contact_number', 'id']
    filter_backends = (filters.SearchFilter,)
    queryset = models.Owner.objects.all()
    serializer_class = serializers.OwnerSerializer

class InterestedViewSet(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    """
    This viewset automatically provides CRUD actions for Interested model.
    """
    search_fields = ['apartment_id', 'flat_id', 'user_id']
    filter_backends = (filters.SearchFilter,)
    queryset = models.Interested.objects.all()
    serializer_class = serializers.InterestedSerializer

class LeaseViewSet(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    """
    This viewset automatically provides CRUD actions for Lease model.
    """
    search_fields = ['lease_start_date', 'lease_end_date']
    filter_backends = (filters.SearchFilter,)
    queryset = models.Lease.objects.all()
    serializer_class = serializers.LeaseSerializer


class ApartmentViewSet(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    """
    This viewset automatically provides CRUD actions for Apartment model.
    """

    search_fields = ['address', 'facilities', 'owner_id']
    filter_backends = (filters.SearchFilter,)
    queryset = models.Apartment.objects.all()
    serializer_class = serializers.ApartmentSerializer