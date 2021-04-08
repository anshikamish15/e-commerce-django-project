from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=30)
    mobile = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
