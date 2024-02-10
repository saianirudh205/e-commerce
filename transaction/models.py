from django.db import models

# Create your models here.

from order.models import Order


class Transaction(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()
    payment_method = models.CharField(max_length=100)
