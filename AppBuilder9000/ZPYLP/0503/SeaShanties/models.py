from django.db import models
from django.db.models import Manager

# Create your models here.


class SeaShanties(models.Model):
    title = models.CharField(max_length=60)
    videoURL = models.URLField()
    lyrics = models.TextField()
    artist = models.CharField(max_length=60)
    year = models.CharField(max_length=60)
    history = models.TextField()

    objects = models.Manager()

    def __str__(self):
        return self.title
