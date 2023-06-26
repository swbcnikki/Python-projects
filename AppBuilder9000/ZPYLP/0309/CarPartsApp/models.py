from django.db import models


MAKE_CHOICES = [
    ('Subaru','Subaru'),
    ('Honda','Honda'),
    ('Toyota','Toyota'),
    ('Ford','Ford'),
    ('Chevy','Chevy'),
    ('Mercedes-benz','Mercedes-benz'),

]

YEAR_CHOICES = [
    ('1990', '1990'),
    ('1995', '1995'),
    ('2000', '2000'),
    ('2005', '2005'),
    ('2010', '2010'),
    ('2015', '2015'),
    ('2020', '2020'),
]

class MyCarParts(models.Model):
    user_name = models.CharField(max_length=60, default="", blank=False, null=False)
    make = models.CharField(max_length=15, default="", choices=MAKE_CHOICES)
    car_Model = models.CharField(max_length=60, default="", blank=True, null=False)
    year = models.CharField(max_length=6, default="", choices=YEAR_CHOICES)
    part = models.TextField(max_length=300, default="", blank=True)
    total = models.DecimalField(default=0.00, max_digits=100000, decimal_places=2)
    image = models.CharField(max_length=255, default='', blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.user_name
