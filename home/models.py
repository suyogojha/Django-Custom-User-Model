from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import *
# Create your models here.

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=12, blank=True)
    is_phone_no_valid = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    
#adding in settings.py    
    
    
    
    
    
    
    
    
    
    

#username: admin@gmail.com
# Password = admin
