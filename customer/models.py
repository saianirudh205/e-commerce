from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    phone = models.CharField(max_length=20)
