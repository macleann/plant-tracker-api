"""Module for Log serializer"""
from rest_framework import serializers
from planttrackerapi.models import Log

class LogSerializer(serializers.ModelSerializer):
    """Serializer for the Log model"""
    class Meta:
        model = Log
        fields = ('id', 'plant', 'date', 'type')
