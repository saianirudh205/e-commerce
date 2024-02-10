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
