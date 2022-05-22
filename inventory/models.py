from django.db import models
from numpy import product

class stockModel(models.Model):
    name = models.CharField(max_length=1000)
    quantity = models.IntegerField()
    buying = models.IntegerField()
    selling = models.IntegerField()
    date = models.DateField()

class orderModel(models.Model):
    seller = models.CharField(max_length=1000)
    buyer = models.CharField(max_length=1000)
    products = models.CharField(max_length=1000000000)
    quantity = models.IntegerField()
    total = models.IntegerField()
    date= models.DateTimeField()