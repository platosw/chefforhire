from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User



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

# the image for chef's profile
class Avatar(models.Model):
    url = models.CharField(max_length=200)
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)

    def __str__(self):
        return f'Photo for chef_id: {self.chef_id} @{self.url}'

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)

    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'pk': self.id})

class Gallery(models.Model):
    url = models.CharField(max_length=200)
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)

    def __str__(self):
        return f'Photo for chef_id: {self.chef_id} @{self.url}'

class Booking(models.Model):
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    host = models.CharField(max_length=30)
    occassion = models.CharField(max_length=100)
    date = models.DateField('Date')
    attendees = models.IntegerField()
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )
   

    def __str__(self):
        return f'{self.get_meal_display()} on {self.date}'

    class Meta:
        ordering = ('-date',)