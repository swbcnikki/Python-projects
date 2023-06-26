from django.db import models
from django import forms


# Create your models here.
class Quotes(models.Model):
    Namerec = models.CharField(max_length=50, default="", blank=True, null=False)
    Address = models.CharField(max_length=100, default="", blank=True, null=False)
    Service_Product = models.CharField(max_length=100, default="What Service or Product is being done?...", blank=True, null=False)
    Description = models.TextField(max_length=500, default="Job Description...", blank=True)
    Details = models.CharField(max_length=200, default="Add Details...", blank=True, null=False)
    Est_cost = models.DecimalField(default=0.00, max_digits=1000000000, decimal_places=2)

    objects = models.Manager()

    def __str__(self):
        return self.Namerec
