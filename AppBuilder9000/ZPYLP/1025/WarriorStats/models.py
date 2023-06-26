from django.db import models

# Create your models here.

PositionTypes = [
    ('PG', 'PG'),
    ('SG', 'SG'),
    ('SF', 'SF'),
    ('PF', 'PF'),
    ('C', 'C')
]


class Player(models.Model):
    Name = models.CharField(max_length=50)
    Position = models.CharField(max_length=50, choices=PositionTypes)
    Points_Per_Game = models.DecimalField(max_digits=15, decimal_places=2)
    Rebounds_Per_Game = models.DecimalField(max_digits=15, decimal_places=2)
    Assists_Per_Game = models.DecimalField(max_digits=15, decimal_places=2)
    Steals_Per_Game = models.DecimalField(max_digits=15, decimal_places=2)

    Players = models.Manager()

    def __str__(self):
        return self.Name
