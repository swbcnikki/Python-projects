from django.db import models


class Trails(models.Model):
    trail_name = models.CharField(max_length=50)
    distance = models.DecimalField(max_digits=5, decimal_places=0, default="")
    state = models.CharField(max_length=50)

    Trail = models.Manager()
