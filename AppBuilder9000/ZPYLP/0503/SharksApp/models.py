from django.db import models


OCEAN_TYPES = [
    ('Atlantic', 'Atlantic'),
    ('Pacific', 'Pacific'),
    ('Indian', 'Indian'),
    ('Arctic', 'Arctic'),
]


CHOICE = [
    ('Yes', 'Yes'),
    ('No', 'No'),
]


class Sharks(models.Model):
    species = models.CharField(max_length=50)
    family = models.CharField(max_length=50)
    diet = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    location = models.CharField(max_length=50, choices=OCEAN_TYPES)
    endangered = models.CharField(max_length=10, choices=CHOICE)

    objects = models.Manager()

    def __str__(self):
        return self.species
