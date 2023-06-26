from django.db import models

# Create your models here.

DIFFICULTY_CHOICES = [
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard'),
]

CAMPING_CHOICES = [
    ('Yes','Yes'),
    ('No','No'),
]

# making blueprint of a type called Trails
class Trails(models.Model):
    name = models.CharField(max_length=40, default="")
    location = models.CharField(max_length=80, default="")
    roundtripMiles = models.DecimalField(default=0.0, max_digits=3, decimal_places=1)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    camping = models.CharField(max_length=10, choices=CAMPING_CHOICES)

    objects = models.Manager()
    def __str__(self):
        return self.name



