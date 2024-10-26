"""
    This is the admin module where you can add admin functionalities. 
    Register your models here.

""" 

from django.contrib import admin
from .models import Apartment, Lease, Flat, User, Interested

# admin.site.register(Owner)
admin.site.register(Apartment)
admin.site.register(Lease)
admin.site.register(Flat)
admin.site.register(User)
admin.site.register(Interested)