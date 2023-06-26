from django.db import models


# Create your models here.
class Activity(models.Model):
    activity_name = models.CharField(max_length=50)
    activity_snacks = models.CharField(max_length=50)
    activity_description = models.CharField(max_length=100)
    distance = models.DecimalField(max_digits=5, decimal_places=0, default="")

    Entries = models.Manager()

    def __str__(self):
        return self.distance


class WeatherMoment(models.Model):
    temperature = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    WeatherMoment = models.Manager()

    def __str__(self):
        return self.date
