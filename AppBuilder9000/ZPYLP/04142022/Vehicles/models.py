from django.db import models

class Vehicles(models.Model):
    year = models.CharField(max_length=4, default="", blank=True)
    vehicle_make = models.CharField(max_length=50, default="", blank=True)
    vehicle_model = models.CharField(max_length=50, default="")
    vehicle_type = models.CharField(max_length=50, default="", blank=True)
    cylinders = models.CharField(max_length=50, default="", blank=True)
    horsepower = models.CharField(max_length=50, default="", blank=True)

    object = models.Manager()

    def __str__(self):
        return self.year + ' ' + self.vehicle_make + ' ' + self.vehicle_model
