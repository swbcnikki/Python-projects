from django.db import models

# Create your models here.
type_choices = [
    ('ATV', 'ATV'),
    ('Motorcycle', 'Motorcycle'),
    ('Side by Side', 'Side by Side'),
]

trail_type = [
    ('Grass', 'Grass'),
    ('Dirt', 'Dirt'),
    ('Concrete', 'Concrete'),
    ('Gravel', 'Gravel'),
    ('Sand', 'Sand'),
    ('Woodchips', 'Woodchips'),
]


class AtvTrails(models.Model):
    trail_name = models.CharField(max_length=50, default="", blank=True)
    vehicle_type = models.CharField(max_length=50, choices=type_choices)
    trail_distance = models.DecimalField(max_digits=4, decimal_places=0, default="")
    trail_terrain = models.CharField(max_length=50, choices=trail_type)
    trail_description = models.TextField(max_length=500, default="")
    city = models.CharField(max_length=50, default="")
    state = models.CharField(max_length=50, default="")

    objects = models.Manager()

    def __str__(self):
        return self.trail_name
