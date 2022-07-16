from django.db import models
from login.manager import UserManager
from django.contrib.auth.models import AbstractUser

class EcomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True,null=True,blank=True)
    phone_number = models.PositiveBigIntegerField(unique=True,null=True,blank=True)
    object = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']
    
