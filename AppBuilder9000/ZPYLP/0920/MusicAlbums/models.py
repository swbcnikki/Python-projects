from django.db import models

# Create your models here.


class Album(models.Model):
    Artist = models.CharField(max_length=50)
    Album = models.CharField(max_length=50)
    Genre = models.CharField(max_length=50)
    Year = models.IntegerField(default='')

    objects = models.Manager()

    def __str__(self):
        return self.Artist + ' ' + self.Album
