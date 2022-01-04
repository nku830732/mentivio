from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=True)
    Phone_No = models.PositiveIntegerField(null=False)
    preparing_for = models.CharField(max_length=50)
    Email = models.CharField(max_length=50,null=False)
    state =  models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=60, blank=True)
    town_or_village = models.CharField(max_length=90, blank=True)
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)           