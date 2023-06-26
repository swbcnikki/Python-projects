from django.db import models


class Stocks(models.Model):
    ticker = models.CharField(max_length=5)
    name = models.CharField(max_length=100)

    objects = models.Manager()

    #   converts the value of ticker to uppercase
    def save(self, *args, **kwargs):
        self.ticker = self.ticker.upper()
        return super(Stocks, self).save(*args, **kwargs)

    #   when referencing the database, the item will be displayed with the value of ticker
    def __str__(self):
        return self.ticker

