from django.db import models


# Create your models here.
HALL_OF_FAME = [
    ('YES', 'Yes'),
    ('NO', 'No'),
]


class Player(models.Model):
    Name = models.CharField(max_length=30)
    Seasons = models.IntegerField(default='')
    Player_Efficiency_Rating = models.DecimalField(max_digits=5, decimal_places=1)
    Points_Per_Game = models.DecimalField(max_digits=5, decimal_places=1)
    Win_Shares = models.DecimalField(max_digits=5, decimal_places=1)
    Hall_of_Fame = models.CharField(max_length=3, choices=HALL_OF_FAME)

    objects = models.Manager()

    def __str__(self):
        return self.Name
