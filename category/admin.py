# in your_app/admin.py
from django.contrib import admin
from .models import Category

# Register your models with the admin site
admin.site.register(Category)

# Repeat this for all your models
