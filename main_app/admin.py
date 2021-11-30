from django.contrib import admin
from .models import Chef, User, Booking, Avatar, Gallery

# Register your models here.
admin.site.register(Chef)
admin.site.register(User)
admin.site.register(Booking)
admin.site.register(Avatar)
admin.site.register(Gallery)