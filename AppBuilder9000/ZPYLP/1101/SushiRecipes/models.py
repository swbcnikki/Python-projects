from django.db import models


# Create your models here.
class SushiRecipes(models.Model):
    style = models.CharField(max_length=60)
    ingredients = models.CharField(max_length=100)
    steps = models.TextField(max_length=200)
    notes = models.CharField(max_length=100)

    objects = models.Manager

    def __str__(self):
        return self.style
