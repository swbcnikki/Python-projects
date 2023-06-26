from django.db import models


class SportsCar(models.Model):
    Year = models.DecimalField(max_digits=4, decimal_places=0)
    Make = models.CharField(max_length=60, default="", blank=True, null=False)
    Model = models.CharField(max_length=60, default="", blank=True, null=False)
    Engine = models.CharField(max_length=60, default="", blank=True, null=False)
    Horsepower = models.DecimalField(max_digits=4, decimal_places=0)
    Top_Speed = models.DecimalField(max_digits=3, decimal_places=0)

    objects = models.Manager()

    def __str__(self):
        return self.Make + ' ' + self.Model

