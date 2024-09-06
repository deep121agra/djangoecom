from django.contrib import admin
from .models import Products, Order
# Register your models here.
# our superuser is admin and password is superuser
admin.site.register(Products)
admin.site.register(Order)
