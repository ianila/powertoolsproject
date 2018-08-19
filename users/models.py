from django.contrib.auth.models import AbstractUser
from django.db import models

class Profile(AbstractUser):
    fullname = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=100, blank=False)
    birthdate = models.DateField(null=True, blank=False)
    nic = models.CharField(max_length=10, blank=False)
    mobilephone = models.CharField(max_length=10, blank=False)
    homephone = models.CharField(max_length=10, blank=False)
    email = models.EmailField(max_length=70,blank=False)
    iscustomer = models.BooleanField(default=True)
    isstaff = models.BooleanField(default=False)
    isroot = models.BooleanField(default=False)

    def __str__(self):
        return self.fullname
