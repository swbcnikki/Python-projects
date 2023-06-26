from django.db import models


# Create your models here.


Type_Choices = [
    ('Comics', 'Comics'),
    ('Graphic novels', 'Graphic novels'),
]


class Cbooks(models.Model):
    type = models.CharField(max_length=60, choices=Type_Choices)
    name = models.CharField(max_length=60, default="", blank=True, null=False)
    description = models.TextField(max_length=300, default="", blank=True)
    price = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2)
    images = models.CharField(max_length=255, default='', blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.name