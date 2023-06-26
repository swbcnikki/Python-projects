from django.db import models

TYPES = [
    ('Acoustic', 'Acoustic'),
    ('Electro-Acoustic', 'Electro-Acoustic'),
    ('Electric', 'Electric'),
    ('Bass', 'Bass'),
]

RATING = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
]


# Create your models here.
class GuitarInfo(models.Model):
    # fields of the model
    type = models.CharField(max_length=50, choices=TYPES)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    stars = models.IntegerField(choices=RATING)
    review = models.TextField(max_length=2000)

    # calls for the brand and model name
    def __str__(self):
        return self.brand + ' ' + self.model

    objects = models.Manager()