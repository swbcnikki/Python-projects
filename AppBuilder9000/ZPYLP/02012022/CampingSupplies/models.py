from django.db import models

color_choices = [
    ('Red', 'Red'),
    ('Blue', 'Blue'),
    ('Orange', 'Orange'),
    ('Yellow', 'Yellow'),
    ('Green', 'Green'),
    ('Purple', 'Purple'),
]

size_choices = [
    ('Extra Small', 'Extra Small'),
    ('Small', 'Small'),
    ('Medium', 'Medium'),
    ('Large', 'Large'),
    ('Extra Large', 'Extra Large'),
]

class Tent(models.Model):
    Color = models.CharField(max_length=30, default="", choices=color_choices)
    PersonCount = models.IntegerField()
    Price = models.FloatField(max_length=30)

    object = models.Manager()

    def __str__(self):
        return self.Color

# Create your models here.
