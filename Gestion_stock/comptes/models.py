from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Utilisateur(AbstractUser):
    phone = models.CharField(max_length=20)
    
    def __str__(self):
        return self.username

