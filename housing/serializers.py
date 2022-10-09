from rest_framework import serializers
from housing import models
from rest_framework.authtoken.models import Token 
from rest_framework.validators import ValidationError
from django.contrib.auth.hashers import make_password

"""
    This is a serializer file to add different serializers for the database.
"""


class UserSerializer(serializers.ModelSerializer):
    """
        This is UserSerializer for User model.
    """
    class Meta:
        """
            This class contains fields to be serialized.
        """
        model = models.User
        fields = '__all__'
    
    def create(self, validated_data):
        """
            This is create method to create the user using password.
        """
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)

class FlatSerializer(serializers.ModelSerializer):
    """
        This is FlarSerializer for Flat model.
    """
    class Meta:
        """
            This class contains fields to be serialized.
        """
        model = models.Flat
        fields = '__all__'

class OwnerSerializer(serializers.ModelSerializer):
    """
        This is OwnerSerializer for Owner model.
    """
    class Meta:
        """
            This class contains fields to be serialized.
        """
        model = models.Owner
        fields = '__all__'

class InterestedSerializer(serializers.ModelSerializer):
    """
        This is InterestedSerializer for Interested model.
    """
    class Meta:
        """
            This class contains fields to be serialized.
        """
        model = models.Interested
        fields = '__all__'


class LeaseSerializer(serializers.ModelSerializer):
    """
        This is LeaseSerializer for Lease model.
    """
    class Meta:
        """
            This class contains fields to be serialized.
        """
        model = models.Lease
        fields = '__all__'

class ApartmentSerializer(serializers.ModelSerializer):
    """
        This is ApartmentSerializer for Apartment model.
    """
    class Meta:
        """
            This class contains fields to be serialized.
        """
        model = models.Apartment
        fields = '__all__'
        
