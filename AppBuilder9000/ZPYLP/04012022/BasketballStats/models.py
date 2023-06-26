from django.db import models


# Create your models here.
class Players(models.Model):
    name = models.CharField(max_length=50)
    seasons_played = models.IntegerField(default='')
    mvp_awards = models.IntegerField(default='')
    championships = models.IntegerField(default='')

    Player = models.Manager()

    def __str__(self):
        return self.name


class Teams(models.Model):
    team_name = models.CharField(max_length=50)
    conference = models.CharField(max_length=10)
    division = models.CharField(max_length=15)

    Team = models.Manager()

    def __str__(self):
        return self.team_name
