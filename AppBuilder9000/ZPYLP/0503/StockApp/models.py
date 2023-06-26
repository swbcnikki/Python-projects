from django.db import models


class WatchStock(models.Model):
    name = models.CharField(max_length=15)
    market_cap = models.CharField(max_length=30)
    time_stamp = models.TimeField(max_length=40)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

        objects = models.Manager()
