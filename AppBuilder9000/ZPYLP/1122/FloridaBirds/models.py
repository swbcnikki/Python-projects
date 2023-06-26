from django.db import models


# Create your models here.


class BirdDescription(models.Model):
    bird_name = models.CharField(max_length=30, blank=True)
    date_seen = models.DateField(blank=True)
    habitat = models.TextField(max_length=100)
    description = models.TextField(max_length=100)
    image = models.TextField(blank=True)

    # BirdDescriptions is the models manager for accessing the dB.
    objects = models.Manager()

    # Below dunder method represents the class object as a string.
    # The bird name ie "stork" will appear in output which makes it easier to read.

    def __str__(self):
        return str(self.bird_name)
