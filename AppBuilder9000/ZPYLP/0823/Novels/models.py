from django.db import models


class Book(models.Model):
    Title = models.CharField(max_length=70, default='')
    Author = models.CharField(max_length=50, default='')
    Series = models.CharField(max_length=50, default='')
    Synopsis = models.TextField(max_length=750, default='')
    Review = models.TextField(max_length=750, default='')
    Rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)

    objects = models.Manager()

    def __str__(self):
        return self.Title
