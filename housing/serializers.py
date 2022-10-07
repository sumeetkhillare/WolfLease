from rest_framework import serializers
from housing import models
from rest_framework.authtoken.models import Token 
from rest_framework.validators import ValidationError

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'

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

class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Apartment
        fields = '__all__'


class LeaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lease
        fields = '__all__'
