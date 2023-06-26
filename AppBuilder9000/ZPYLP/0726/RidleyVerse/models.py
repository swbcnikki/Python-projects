from django.db import models


class Movie(models.Model):
    FilmName = models.CharField(max_length=100)
    ReleaseYear = models.IntegerField(blank=True)
    StarNames = models.CharField(max_length=100, blank=True)
    DirectorName = models.CharField(max_length=60, blank=True)
    MovieSummary = models.TextField(blank=True)

    # using the models manager to return the name of film.
    objects = models.Manager()

    def __str__(self):
        return self.FilmName
