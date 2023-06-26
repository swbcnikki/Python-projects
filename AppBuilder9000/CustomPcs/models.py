from django.db import models
from django import forms

# Create your models here.
Case_Sizes = (
    ('full tower', 'Full Tower'),
    ('mid-tower', 'Mid-Tower'),
    ('mini-tower', 'Mini-Tower'),
    ('small form factor', 'Small Form Factor'),
)


class Builds(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    case_size = models.CharField( max_length=30, choices=Case_Sizes)
    Specifications = models.TextField(max_length=255, default='')

    Builds = models.Manager()

    def __str__(self):
        return self.first_name
