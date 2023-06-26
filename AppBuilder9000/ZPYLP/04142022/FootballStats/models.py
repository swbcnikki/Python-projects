from django.db import models




# Create your models here.
class Players(models.Model):
    name = models.CharField(max_length=50)
    team = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    passing_yards = models.IntegerField(default='')
    touchdowns = models.IntegerField(default='')
    rushing_yards = models.IntegerField(default='')
    receptions = models.IntegerField(default='')
    tackles = models.IntegerField(default='')
    sacks = models.IntegerField(default='')
    interceptions = models.IntegerField(default='')

    Player = models.Manager()

    def __str__(self):
        return self.name


from django.db import models

# Create your models here.
class Stats(models.Model):
    team = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    passing_yards = models.IntegerField(default='')
    touchdowns = models.IntegerField(default='')
    rushing_yards = models.IntegerField(default='')
    receptions = models.IntegerField(default='')
    tackles = models.IntegerField(default='')
    sacks = models.IntegerField(default='')
    interceptions = models.IntegerField(default='')

    Stat = models.Manager()

    def __str__(self):
        return self.stat_name
