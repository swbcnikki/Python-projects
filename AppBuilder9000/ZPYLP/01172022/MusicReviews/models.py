from django.db import models
from django import forms


TYPE_CHOICES = [
    ('1 star', '1 star'),
    ('2 star', '2 star'),
    ('3 star', '3 star'),
    ('4 star', '4 star'),
    ('5 star', '5 star'),
]


# Create your models here.
class Review(models.Model):
    Artist = models.CharField(max_length=50, default="", blank=True, null=False)
    Album = models.CharField(max_length=50, default="", blank=True, null=False)
    Song = models.CharField(max_length=50, default="", blank=True, null=False)
    Review = models.TextField(max_length=300, default="", blank=True, null=False)
    Stars = models.CharField(max_length=10, choices=TYPE_CHOICES)

    objects = models.Manager()

    def __str__(self):
        return self.Artist

