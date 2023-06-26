from django.db import models


# Create your models here.


class HardRock(models.Model):
    Band = models.CharField(max_length=60)
    member = models.CharField(max_length=60)
    Genre = models.CharField(max_length=60)
    Instrument = models.CharField(max_length=60)

    objects = models.Manager()

    def __str__(self):
        return self.member
