from django.contrib import admin

# Register your models here.
from inventory.models import *

admin.site.register(stockModel)
admin.site.register(orderModel)