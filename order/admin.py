# in your_app/admin.py
from django.contrib import admin
from .models import Order, OrderDetail

# Register your models with the admin site
admin.site.register(Order)
admin.site.register(OrderDetail)
# Repeat this for all your models
