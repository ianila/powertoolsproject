from django.db import models
from users.models import Profile

class Tool(models.Model):
    serialno = models.CharField(max_length=16, blank=False, null=False)
    make = models.CharField(max_length=16, blank=False, null=False)
    rentalvalue = models.DecimalField(max_digits=7, decimal_places=2)
    desc = models.TextField(blank=True, null=True)

class Photo(models.Model):
    photo = models.FileField(upload_to='tools/')
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)    

class Rent(models.Model):
    rent_date = models.DateField()
    return_date = models.DateField()
    value = models.DecimalField(max_digits=7, decimal_places=2)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE)
