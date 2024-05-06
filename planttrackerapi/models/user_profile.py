"""Module for extending the User model"""
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """Model for User Profile"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image_url = models.CharField(max_length=200, blank=True, null=True)
    zip_code = models.CharField(max_length=5, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
