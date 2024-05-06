"""Module for Log model"""
from django.db import models

class Log(models.Model):
    """Model for Log"""
    plant=models.ForeignKey("Plant", on_delete=models.CASCADE)
    date=models.DateField()
    type=models.CharField(max_length=50)
