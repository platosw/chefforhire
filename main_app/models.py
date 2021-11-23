from django.db import models
from django.db.models.fields import CharField


MEALS = (
    ('B', 'Breakfast'),
    ('R', 'Brunch'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)
# Create your models here.

# for Push for Alex

class Chef(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    bio = models.TextField(max_length=500)
    location = models.CharField(max_length=100)
    hourly = models.IntegerField()
    phone = models.CharField(max_length=12)
    booked_dates = models.DateField('Booked Dates')


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    
class Booking(models.Model):
    occassion = models.CharField(max_length=100)
    date = models.DateTimeField('Booking')
    attendees = models.IntegerField()
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )
    




    

