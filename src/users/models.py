from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from .utils import user_directory_path

from localflavor.in_.forms import INStateSelect, INZipCodeField
from django.core.validators import RegexValidator




class Location(models.Model):
    address_1=models.CharField(max_length=128, blank=True)
    address_2=models.CharField(max_length=128, blank=True)
    state = models.CharField(max_length=50, blank=True) 
    city = models.CharField(max_length=64)  # Add this line
    zip_code = models.CharField(
        max_length=6,
        blank=True,  # Allow this field to be blank
        null=True,   # Optionally allow null if that's what you want
    )
    def __str__(self):
        return f'Location {self.id}'

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    photo=models.ImageField(upload_to=user_directory_path, null=True)
    bio=models.CharField(max_length=140, blank=True)
    phone_number=models.CharField(max_length=12, blank=True)
    location=models.OneToOneField(Location,on_delete=models.SET_NULL,null=True) 
    
    photo=models.ImageField(upload_to=user_directory_path, null=True)
    
    
    def  __str__(self):
        return f'{self.user.username}\'s Profile'

# Create your models here.
