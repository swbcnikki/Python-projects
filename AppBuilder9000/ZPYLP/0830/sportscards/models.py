from django.db import models


class Card(models.Model):
    Player = models.CharField(max_length=70, default='')
    Year = models.IntegerField(default='')
    Team = models.CharField(max_length=50, default='')
    Brand = models.CharField(max_length=750, default='')

    objects = models.Manager()

    def __str__(self):
        return self.Player
