from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    nickname=models.CharField(max_length=100)
    university=models.CharField(max_length=50)
    resident_registration_number = models.CharField(max_length=13, blank=True)

    def get_gender(self):
        seventh_digit = int(self.resident_registration_number[6])
        if seventh_digit == 2 or seventh_digit == 4:
            return '여자'
        else: 
            return '남자'
    
    def __str__(self):
        return self.username