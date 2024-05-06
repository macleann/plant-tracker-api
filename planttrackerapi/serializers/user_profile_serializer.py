"""Module for User Profile serializer"""
from rest_framework import serializers
from planttrackerapi.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for the User Profile model"""
    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'profile_image_url', 'zip_code', 'created_on', 'modified_on')
        depth = 1
