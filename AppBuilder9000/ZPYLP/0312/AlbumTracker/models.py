from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=60)
    artist = models.CharField(max_length=60)
    date_listened = models.DateField()
    notes = models.TextField()

    objects = models.Manager()

    class Meta:
        ordering = ['artist']

    def __str__(self):
        return self.title
