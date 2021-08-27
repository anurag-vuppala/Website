from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.utils import tree


class UserInterest(models.Model):
    name = models.CharField(max_length=64,unique=True)
    normalized_name = models.CharField(max_length=64,unique=True)
    

class UserPersona(models.Model):
    name = models.CharField(max_length=64,unique=True)
    normalized_name = models.CharField(max_length=64,unique=True)
    description = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

# create model here

class UserProfile(models.Model):
    #owner
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
     #settings
    is_full_name_dsiplayed = models.BooleanField(default=True)

    #details
    bio = models.CharField(max_length=500, blank=True, null=True)
    website = models.URLField(max_length=200, blank = True, null=True)
    persona = models.ForeignKey(UserPersona, on_delete=models.SET_NULL, blank=True, null= True)
    interest= models.ManyToManyField(UserInterest,blank=True)