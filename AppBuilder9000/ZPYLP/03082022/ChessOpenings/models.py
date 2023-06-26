from django.db import models


# Create your models here.
class Games(models.Model):

    title = models.CharField(max_length=50, blank=True)
    playerWhite = models.CharField(max_length=50)
    playerBlack = models.CharField(max_length=50)
    yearPlayed = models.IntegerField(blank=True)
    PGN = models.TextField(max_length=500)
    winner = models.CharField(max_length=10)

    Game = models.Manager()

    def __str__(self):
        return self.title or "{}, {}".format(self.playerWhite, self.playerBlack)


from django.db import models

# Create your models here.
