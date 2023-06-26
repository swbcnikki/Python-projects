from django.db import models


# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)

    Entries = models.Manager()

    def __str__(self):
        return self.title


class WeatherMoment(models.Model):
    temperature = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    WeatherMoments = models.Manager()

    def __str__(self):
        return self.date
