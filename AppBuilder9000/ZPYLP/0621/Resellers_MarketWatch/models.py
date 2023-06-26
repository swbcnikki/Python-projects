from django.db import models
from django import forms



# Create your models here.

Categories = [
    (None, 'Select Category'),
    ('Electronics', 'Electronics'),
    ('Pet Supplies', 'Pet Supplies'),
    ('Vehicles', 'Vehicles'),
]


class WebScrape(models.Model):
    DoesNotExist = None
    category = models.CharField(max_length=50, null=False, choices=Categories)
    url = models.URLField(max_length=200, default='', null=False)
    date = models.DateField(auto_now_add=False)
    price = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, null=False)
    imageUrl = models.URLField(max_length=200)
    profit = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, null=False)

    WebScrape_db = models.Manager()

    def __str__(self):
        return self.category


class UserLogin(models.Model):
    DoesNotExist = None
    first_name = models.CharField(max_length=200, default='', null=False)
    last_name = models.CharField(max_length=200, default='', null=False)
    email = models.CharField(max_length=200, default='')

    User = models.Manager()

    def __str__(self):
        return self.first_name






