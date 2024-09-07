from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100, blank=True)
    profile_img = models.ImageField(upload_to='profile_images', default='default/blank-profile-picture.png')
    phone_number = models.CharField(max_length=13, blank=True)
    
    def __str__(self) :
        return self.user.username