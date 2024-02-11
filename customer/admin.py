# in your_app/admin.py
from django.contrib import admin
from .models import Customer

# Register your models with the admin site
admin.site.register(Customer)

# Repeat this for all your models
