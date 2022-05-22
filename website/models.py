from unicodedata import category
from django.db import models
from numpy import number

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=10000,default=None)
    category = models.CharField(max_length=1000,default=None)
    description = models.CharField(max_length=100000,default="none")
    price = models.IntegerField(default=None)
    seller = models.CharField(max_length=1000,default=None)
    available = models.BooleanField(default=True)
    date = models.DateField(default=None)
    negotiable = models.BooleanField(default=True)
    photo = models.ImageField()

class driver(models.Model):
    first = models.CharField(max_length=1000)
    last = models.CharField(max_length=1000)
    id_number = models.IntegerField(default=None)
    type = models.CharField(max_length=1000)
    number = models.IntegerField()