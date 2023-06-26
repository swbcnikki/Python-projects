from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30)
    product_number = models.IntegerField(default="1")
    summary = models.CharField(max_length=50)
    product_price = models.IntegerField(default="1")

    object = models.Manager()
