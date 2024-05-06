"""Serializer for the Plant model."""
from rest_framework import serializers
from planttrackerapi.models import Plant

class PlantSerializer(serializers.ModelSerializer):
    """Serializer for the Plant model"""
    class Meta:
        model = Plant
        fields = ('id', 'name', 'nickname', 'photo_url', 'water_freq', 'fert_freq', 'sunlight', 'note', 'user')
