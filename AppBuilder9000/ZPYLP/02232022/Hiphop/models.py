from django.db import models
from django import forms

TYPE_CHOICES = [
    ('1 mic', '1 mic'),
    ('2 mic', '2 mic'),
    ('3 mic', '3 mic'),
    ('4 mic', '4 mic'),
    ('5 mic', '5 mic'),
]


class Choice(models.Model):
    eighties = models.CharField(max_length=50, default="", blank=True, null=False)
    nineties = models.CharField(max_length=50, default="", blank=True, null=False)
    two_thousand = models.CharField(max_length=50, default="", blank=True, null=False)
    today = models.TextField(max_length=300, default="", blank=True, null=False)
    mics = models.CharField(max_length=10, choices=TYPE_CHOICES)

    objects = models.Manager()

    def __str__(self):
        return self.mics
