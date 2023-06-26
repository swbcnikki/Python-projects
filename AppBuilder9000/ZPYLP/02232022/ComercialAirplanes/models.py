from django.db import models
from django.forms import ModelForm



# To provide choices for inpput user
Manufacture = [
    ('Boeing', 'Boeing'),
    ('Airbus', 'Airbus'),
    ('Bombardier', 'Bombardier'),
    ]

#to provide choices for inpput user

Type = [
    ('Widebody', 'Widebody'),
    ('Narrowbody', 'Narrowbody'),
]

#to provide choices for inpput user

Propulsion = [
    ('Jet', 'Jet'),
    ('Turboprop', 'Turboprop'),
]

class Airplane(models.Model):
    Propulsion = models.CharField(max_length=20, default='', choices=Propulsion)
    Manufacture = models.CharField(max_length=20, default='', choices=Manufacture)
    AircraftType = models.CharField(max_length=20, default='', choices=Type)
    ModelNumber = models.CharField(max_length=20, default='')
    Price = models.DecimalField(default=0.00, max_digits=20, decimal_places=2)

    Plane = models.Manager()

    def __str__ (self):
        return self.Manufacture

