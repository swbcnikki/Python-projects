from django.db import models


STATE_CHOICES = [
    ('OR', 'OR'),
    ('WA', 'WA'),
]

TYPE_CHOICES = [
    ('Dispersed', 'Dispersed'),
    ('Developed', 'Developed'),
]

ACCESS_CHOICES = [
    ('Drive-up', 'Drive-up'),
    ('Hike-in', 'Hike-in'),
]

RATING_CHOICES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
]


class Campsite(models.Model):
    name = models.CharField(max_length=100, unique=True)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    type = models.CharField(max_length=9, choices=TYPE_CHOICES)
    access = models.CharField(max_length=8, choices=ACCESS_CHOICES)
    fee = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    directions = models.CharField(max_length=500, null=True, blank=True)

    Campsites = models.Manager()

    def __str__(self):
        return self.name + "," + self.state





