from django.db import models
from django.db.models import Manager


class TravelDestinations(models.Model):
    City_Name = models.CharField(max_length=200)
    Country_Name = models.CharField(max_length=200)
    Activity = models.CharField(max_length=300)
    Travel_Date = models.DateField(blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.City_Name


from django.db import models

# Create your models here.
