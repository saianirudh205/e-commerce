# in your_app/admin.py
from django.contrib import admin
from .models import Product

# Register your models with the admin site
admin.site.register(Product)

# Repeat this for all your models
