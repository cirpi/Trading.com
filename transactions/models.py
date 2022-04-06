from codecs import backslashreplace_errors
from operator import mod
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Stock(models.Model):
    ticker = models.CharField(max_length=20)
    name = models.CharField(max_length=300)

    def __str__(self) -> str:
        return f'{self.ticker} {self.name}'

class Asset(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, related_name='stock', on_delete=models.CASCADE)
    quantity = models.FloatField()
    price = models.FloatField(verbose_name='Price per stock')
    sum = models.FloatField(default=0)

    def __str__(self) -> str:
        return f'{self.stock.ticker} {self.quantity} {self.price}'


class Balance(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='balance')
    total = models.FloatField(default=10000)

    def __str__(self) -> str:
        return f'{self.user.username} {self.total}'