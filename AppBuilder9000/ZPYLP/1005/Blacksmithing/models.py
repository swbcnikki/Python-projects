from django.db import models

USE_LIST = [
    ('Handling', 'Handling'),
    ('Shaping', 'Shaping'),
    ('Removing Material', 'Removing Material'),
    ('Not Part of the Tang', 'Not Part of the Tang'),
    ('Other (Please specify in description)', 'Other (Please specify in description)')
]


class Tool(models.Model):
    name = models.CharField(max_length=60)
    use = models.CharField(max_length=60, choices=USE_LIST)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    link = models.TextField(max_length=600)
    description = models.TextField(max_length=600)

    objects = models.Manager()

    def __str__(self):
        return self.name
