from django.db import models

# Created models here
GREEN_CHOICES = [
    ('Electric', 'Electric'),
    ('Hybrid', 'Hybrid'),
]

COLOR_CHOICES = [
    ('Red', 'Red'),
    ('White', 'White'),
    ('Gold', 'Gold'),
    ('Silver', 'Silver'),
    ('Black', 'Black'),
]

class Vehicle(models.Model):
    brand = models.CharField(max_length=100, blank=False, null=False) #vehicle name is required
    green = models.CharField(max_length=50, choices=GREEN_CHOICES)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=100, choices=COLOR_CHOICES)

    Vehicle = models.Manager()

    def __str__(self):
        return self.brand




