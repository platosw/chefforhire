from django.db import models


# Create your models here.
class Chef(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    bio = models.TextField(max_length=500)
    location = models.CharField(max_length=100)
    shift = models.CharField(max_length=20)
    hourly = models.IntegerField()
    phone = models.CharField(max_length=12)
    booked_dates = models.DateTimeField('Booked Dates')



    