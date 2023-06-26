from django.db import models

'''Adding choices for a drop down menu controlling user what to edit'''
TYPE_CHOICES = (
    ('benches', 'benches'),
    ('treadmills', 'treadmills'),
    ('stationary bikes', 'stationary bikes'),
    ('Free weights', 'Free weights'),
    ('Mechanical weight set', 'Mechanical weight set'),
    ('Racks', 'Racks'),

)
'''mapping our db model'''


class WorkoutEquipment(models.Model):
    type = models.CharField(max_length=60, choices=TYPE_CHOICES)
    name = models.CharField(max_length=60, default="", blank=True, null=False)
    description = models.TextField(max_length=300, default="", blank=True)
    price = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2)
    image = models.CharField(max_length=255, default="", blank=True)

    objects = models.Manager()


'''This puts the name as the title of the the field'''

def __str__(self):
    return self.name