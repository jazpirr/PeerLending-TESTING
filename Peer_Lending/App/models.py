from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True) 
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)

    USERNAME_FIELD = "email"  
    REQUIRED_FIELDS = ["first_name", "last_name"] 
    def __str__(self):
        return self.email
