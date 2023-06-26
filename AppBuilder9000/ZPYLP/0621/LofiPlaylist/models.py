from django.db import models
from django.forms import ModelForm


class Song(models.Model):
    name = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    year = models.IntegerField(default=1991)

    objects = models.Manager()

    def __str__(self):
        return self.name



