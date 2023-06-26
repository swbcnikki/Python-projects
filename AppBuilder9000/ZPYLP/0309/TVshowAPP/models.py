from django.db import models

# Create your models here.

class TVshows(models.Model):
    show_name = models.CharField(max_length=100)
    genre = models.CharField(max_length=60)
    network = models.CharField(max_length=60)
    seasons = models.PositiveIntegerField()
    summary = models.TextField(max_length=500, default="What is the show about?")


    objects = models.Manager()

    def __str__(self):
        return self.show_name



