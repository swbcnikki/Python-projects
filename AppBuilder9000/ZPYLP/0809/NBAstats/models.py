from django.db import models

# Dictionary
YEAR_CHOICES = [
    ("2020-2021", "2020-2021"),
    ("2019-2020", "2019-2020"),
    ("2018-2019", "2018-2019"),
]


# Create your models here.
class Defensive_Stats(models.Model):
    year = models.CharField(max_length=10, choices=YEAR_CHOICES)
    playerName = models.CharField(max_length=60, blank=False, null=False)
    defRebs = models.IntegerField(blank=False, null=False, default=0)
    steals = models.IntegerField(blank=False, null=False, default=0)
    blocks = models.IntegerField(blank=False, null=False, default=0)

    objects = models.Manager()

    def __str__(self):
        return self.playerName


class PlayerDb(models.Model):
    playerName = models.CharField(max_length=60, blank=False, null=False)
    defRebs = models.IntegerField(blank=False, null=False, default=0)
    steals = models.IntegerField(blank=False, null=False, default=0)
    blocks = models.IntegerField(blank=False, null=False, default=0)
    total = models.IntegerField(blank=False, null=False, default=0)

    objects = models.Manager()

    def __str__(self):
        return self.playerName


class FavoritesDB(models.Model):
    playerName = models.CharField(max_length=60, blank=False, null=False)
    defRebs = models.IntegerField(blank=False, null=False, default=0)
    steals = models.IntegerField(blank=False, null=False, default=0)
    blocks = models.IntegerField(blank=False, null=False, default=0)
    total = models.IntegerField(blank=False, null=False, default=0)

    objects = models.Manager()

    def __str__(self):
        return self.playerName
