from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    image_small = models.ImageField(upload_to='avatars/', null=True, blank=True)
    image_medium = models.ImageField(upload_to='avatars/', null=True, blank=True)
    image_large = models.ImageField(upload_to='avatars/', null=True, blank=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email
    