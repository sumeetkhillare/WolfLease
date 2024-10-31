"""
    This is a file to add views for models. 
"""

from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework import filters, viewsets, generics
from django.contrib.auth.decorators import login_required
from housing import serializers
from django.contrib.auth import authenticate, login, logout
from housing import models
from django.utils.decorators import method_decorator
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password
from rest_framework import status



# # Create your views here.
# class UserViewSet(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
#     """
#     This viewset automatically provides CRUD actions for User model.
#     """

# # Add search fields to the user view set
#     search_fields = ['contact_email', 'contact_number']
#     '''Search fields for Userviewset''' 
#     filter_backends = (filters.SearchFilter,)
#     '''This is used for filtering Userviewset'''
#     queryset = models.User.objects.all()
#     '''Database query parameters Userviewset'''
#     serializer_class = serializers.UserSerializer

# class FlatViewSet(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
#     """
#     This viewset automatically provides CRUD actions for Flat model.
#     """
#     search_fields = ['availability', 'rent_per_room']
#     '''Search fields for Flatviewset''' 
#     filter_backends = (filters.SearchFilter,)
#     '''This is used for filtering Flatviewset'''
#     queryset = models.Flat.objects.all()
#     '''Database query parameters Flatviewset'''
#     serializer_class = serializers.FlatSerializer

# class OwnerViewSet(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
#     """
#     This viewset automatically provides CRUD actions for Owner model.
#     """
#     search_fields = ['contact_email', 'contact_number', 'id']
#     '''Search fields for Ownerviewset''' 
#     filter_backends = (filters.SearchFilter,)
#     '''This is used for filtering Ownerviewset'''
#     queryset = models.Owner.objects.all()
#     '''Database query parameters Ownerviewset'''
#     serializer_class = serializers.OwnerSerializer

# class InterestedViewSet(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
#     """
#     This viewset automatically provides CRUD actions for Interested model.
#     """
#     search_fields = ['apartment_id', 'flat_id', 'user_id']
#     '''Search fields for Interestedviewset''' 
#     filter_backends = (filters.SearchFilter,)
#     '''This is used for filtering Interestedviewset'''
#     queryset = models.Interested.objects.all()
#     '''Database query parameters Interestedviewset'''
#     serializer_class = serializers.InterestedSerializer

# class LeaseViewSet(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
#     """
#     This viewset automatically provides CRUD actions for Lease model.
#     """
#     search_fields = ['lease_start_date', 'lease_end_date']
#     '''Search fields for Leaseviewset''' 
#     filter_backends = (filters.SearchFilter,)
#     '''This is used for filtering Leaseviewset'''
#     queryset = models.Lease.objects.all()
#     '''Database query parameters Leaseviewset'''
#     serializer_class = serializers.LeaseSerializer


# class ApartmentViewSet(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
#     """
#     This viewset automatically provides CRUD actions for Apartment model.
#     """

#     search_fields = ['address', 'facilities', 'owner_id']
#     '''Search fields for Apartmentviewset''' 
#     search_fields = ['address', 'facilities']
#     filter_backends = (filters.SearchFilter,)
#     '''This is used for filtering Apartmentviewset'''
#     queryset = models.Apartment.objects.all()
#     '''Database query parameters Apartmentviewset'''
#     serializer_class = serializers.ApartmentSerializer


class UserLogin(APIView):
    """
    API View for user login
    """
    def post(self, request):
        contact_email = request.data.get('contact_email')
        password = request.data.get('password')

        try:
            user = models.User.objects.get(contact_email=contact_email)
            print(user.password, password)
            if password == user.password:
                login(request, user)
                
                session_id = request.session.session_key
                # session_id = "2"
                
                return Response(
                    {
                        'message': 'Login successful',
                        'user_id': str(user.id),
                        'sessionid': session_id
                    },
                    status=status.HTTP_200_OK
                )
                
                # return Response({'message': 'Login successful', 'user_id': str(user.id)}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        except models.User.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

class UserLogout(APIView):
    """
    API View for user logout
    """
    def post(self, request):
        # Handle logout logic, e.g., clearing session data, etc.
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)

# @method_decorator(login_required, name='dispatch')
class FlatViewSet(viewsets.ModelViewSet):
    queryset = models.Flat.objects.all()
    serializer_class = serializers.FlatSerializer

# @method_decorator(login_required, name='dispatch')
class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

class LeaseViewSet(viewsets.ModelViewSet):
    queryset = models.Lease.objects.all()
    serializer_class = serializers.LeaseSerializer

class InterestViewSet(viewsets.ModelViewSet):
    queryset = models.Interested.objects.all()
    serializer_class = serializers.InterestedSerializer

@api_view(['POST'])
def sign_lease(request, lease_identifier, username, dob):
    lease = models.Lease.objects.get(lease_identifier=lease_identifier)
    user = models.User.objects.get(username=username)
    if str(user.dob) == (dob):
        lease.is_signed = True
        lease.save()
    
    # Return a JSON response confirming the update
    return JsonResponse({
        "message": f"Lease with identifier {lease_identifier} has been signed.",
        "is_signed": lease.is_signed
    })

class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = models.Apartment.objects.all()
    serializer_class = serializers.ApartmentSerializer

# @method_decorator(login_required, name='dispatch1')
# class OwnerViewSet(viewsets.ModelViewSet):
#     queryset = models.Owner.objects.all()
#     serializer_class = serializers.OwnerSerializer