# in your_app/admin.py
from django.contrib import admin
from .models import Transaction

# Register your models with the admin site
admin.site.register(Transaction)
# admin.site.register(YourModel2)
# Repeat this for all your models
