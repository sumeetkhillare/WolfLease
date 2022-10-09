from rest_framework import serializers
from housing import models
from rest_framework.authtoken.models import Token 
from rest_framework.validators import ValidationError
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)

class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Flat
        fields = '__all__'

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Owner
        fields = '__all__'

class InterestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Interested
        fields = '__all__'


class LeaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lease
        fields = '__all__'

class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Apartment
        fields = '__all__'
        
