"""
    This is a file to add views for models. 
"""

from django.shortcuts import render
from rest_framework import filters, viewsets, generics
from housing import serializers
from housing import models
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class UserViewSet(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    """
    This viewset automatically provides CRUD actions for User model.
    """

# Add search fields to the user view set
    search_fields = ['contact_email', 'contact_number']
    '''Search fields for Userviewset''' 
    filter_backends = (filters.SearchFilter,)
    '''This is used for filtering Userviewset'''
    queryset = models.User.objects.all()
    '''Database query parameters Userviewset'''
    serializer_class = serializers.UserSerializer

class FlatViewSet(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    """
    This viewset automatically provides CRUD actions for Flat model.
    """
    search_fields = ['availability', 'rent_per_room']
    '''Search fields for Flatviewset''' 
    filter_backends = (filters.SearchFilter,)
    '''This is used for filtering Flatviewset'''
    queryset = models.Flat.objects.all()
    '''Database query parameters Flatviewset'''
    serializer_class = serializers.FlatSerializer

class OwnerViewSet(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    """
    This viewset automatically provides CRUD actions for Owner model.
    """
    search_fields = ['contact_email', 'contact_number', 'id']
    '''Search fields for Ownerviewset''' 
    filter_backends = (filters.SearchFilter,)
    '''This is used for filtering Ownerviewset'''
    queryset = models.Owner.objects.all()
    '''Database query parameters Ownerviewset'''
    serializer_class = serializers.OwnerSerializer

class InterestedViewSet(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    """
    This viewset automatically provides CRUD actions for Interested model.
    """
    search_fields = ['apartment_id', 'flat_id', 'user_id']
    '''Search fields for Interestedviewset''' 
    filter_backends = (filters.SearchFilter,)
    '''This is used for filtering Interestedviewset'''
    queryset = models.Interested.objects.all()
    '''Database query parameters Interestedviewset'''
    serializer_class = serializers.InterestedSerializer

class LeaseViewSet(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    """
    This viewset automatically provides CRUD actions for Lease model.
    """
    search_fields = ['lease_start_date', 'lease_end_date']
    '''Search fields for Leaseviewset''' 
    filter_backends = (filters.SearchFilter,)
    '''This is used for filtering Leaseviewset'''
    queryset = models.Lease.objects.all()
    '''Database query parameters Leaseviewset'''
    serializer_class = serializers.LeaseSerializer


class ApartmentViewSet(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    """
    This viewset automatically provides CRUD actions for Apartment model.
    """

    search_fields = ['address', 'facilities', 'owner_id']
    '''Search fields for Apartmentviewset''' 
    search_fields = ['address', 'facilities']
    filter_backends = (filters.SearchFilter,)
    '''This is used for filtering Apartmentviewset'''
    queryset = models.Apartment.objects.all()
    '''Database query parameters Apartmentviewset'''
    serializer_class = serializers.ApartmentSerializer