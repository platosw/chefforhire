from django.db import models
from django.urls import reverse
from datetime import date



MEALS = (
    ('B', 'Breakfast'),
    ('R', 'Brunch'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Chef(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=50)
    bio = models.TextField(max_length=500)
    location = models.CharField(max_length=100)
    hourly = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('chef_detail', kwargs={'pk': self.id})

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)

    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'pk': self.id})

class Booking(models.Model):
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    occassion = models.CharField(max_length=100)
    date = models.DateField('Booking')
    attendees = models.IntegerField()
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )