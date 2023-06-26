from django.db import models
from .Subject import SUBJECT

# Create your models here.
class Quote(models.Model):
    Author = models.CharField(max_length=30)
    Quote = models.CharField(max_length=1000)
    Year = models.IntegerField()
    subject = models.CharField(max_length=50, null=False, choices=SUBJECT)

    objects = models.Manager()

    def __str__(self):
        return self.name
