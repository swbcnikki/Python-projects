from django.db import models
from django import forms

# Create your models here.

meas_choices = (
    ('cups','cups'),
    ('tablespoons','tablespoons'),
    ('teaspoon', 'teaspoon'),
    ('ounces', 'ounces'),
    ('grams', 'grams'),
)

class Convert(models.Model):
    recipeName = models.CharField(max_length=250, default="", blank=True, null=False)
    amount = models.DecimalField(max_length=0.00, max_digits=1000, decimal_places=2)
    measurement = models.CharField(max_length=60, choices=meas_choices)

    objects = models.Manager()

    def __str__(self):
        return self.recipeName