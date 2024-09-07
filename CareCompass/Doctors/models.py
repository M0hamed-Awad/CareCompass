from django.db import models
from datetime import date
from django.conf import settings
import os

# Create your models here.

class DoctorProfile(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    full_name_in_english = models.CharField(max_length=100)
    full_name_in_arabic = models.CharField(max_length=100)
    doctor_profile_img = models.ImageField(upload_to='doctors_profile_images', blank=True, null=True)
    english_bio = models.TextField()
    arabic_bio = models.TextField()
    phone = models.CharField(max_length=13)
    address_in_english = models.CharField(max_length=255)
    address_in_arabic = models.CharField(max_length=255)
    specialization_in_english = models.CharField(max_length=100)
    specialization_in_arabic = models.CharField(max_length=100)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    birthdate = models.DateField()
    
    
    default_pic_mapping = {
        'Male': 'default/male_blank_doctor.png',
        'Female': 'default/female_blank_doctor.png'
    }
    
    def get_profile_pic_url(self):
        if not self.doctor_profile_img:
            return os.path.join(settings.MEDIA_URL, self.default_pic_mapping[self.gender])
        return self.doctor_profile_img.url
    
    @property
    def age(self):
        today = date.today()
        return today.year - self.birthdate.year
    
    
    def __str__(self):
        return self.full_name_in_english