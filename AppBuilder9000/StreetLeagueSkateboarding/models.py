# Imports;
from django.db import models

# Models;
class Skater(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    hometown = models.CharField(max_length=50)

    # Model Manager;
    Entry = models.Manager()

    # str() Method;
    def __str__(self):
        return self.first_name + '' + self.last_name

class WeatherMoment(models.Model):
    temperature = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    WeatherMoments = models.Manager()

    def __str__(self):
        return self.date