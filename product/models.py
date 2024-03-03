from django.utils import timezone
from django.db import models

# Create your models here.
from category.models import Category


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock_quantity = models.IntegerField(default=0)
    image_url = models.URLField()
    created_date = models.DateTimeField(auto_now_add=True, null=True)  # Automatically set on creation
    updated_date = models.DateTimeField(auto_now=True, null=True)      # Automatically updated on every save
    


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_date = models.DateTimeField(auto_now_add=True, null=True)  # Automatically set on creation
    updated_date = models.DateTimeField(auto_now=True, null=True)      # Automatically updated on every save
