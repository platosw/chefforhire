from django.contrib import admin
from .models import Chef, User, Booking

# Register your models here.
admin.site.register(Chef)
admin.site.register(User)
admin.site.register(Booking)