from django.db import models

# Create your models here.
position_choices = (
    ('pg', 'Point Guard'),
    ('sg', 'Shooting Guard'),
    ('sf', 'Small Forward'),
    ('pf', 'Power Forward'),
    ('c', 'Center')
)


class Pickup(models.Model):
    name = models.CharField(max_length=50, null=True)
    position = models.CharField(max_length=30, choices=position_choices, default='Point Guard')
    date = models.DateField(auto_now=True)
    points = models.PositiveIntegerField()
    assists = models.PositiveIntegerField()
    rebounds = models.PositiveIntegerField()
    steals = models.PositiveIntegerField()
    blocks = models.PositiveIntegerField()
    turnovers = models.PositiveIntegerField()

    games = models.Manager()
