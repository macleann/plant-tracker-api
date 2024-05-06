"""Module for Plant model"""
from django.db import models
from django.contrib.auth.models import User

class Plant(models.Model):
    """Model for Plant"""
    name=models.CharField(max_length=50)
    nickname=models.CharField(max_length=50, blank=True, null=True)
    photo_url=models.CharField(max_length=200, blank=True, null=True)
    water_freq=models.IntegerField()
    fert_freq=models.IntegerField()
    sunlight=models.IntegerField()
    note=models.TextField(blank=True, null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
