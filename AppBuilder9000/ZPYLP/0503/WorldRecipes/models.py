from django.db import models


class Recipe(models.Model):
    cuisine_type = models.CharField(max_length=30)
    recipe_name = models.CharField(max_length=30)
    ingredients = models.CharField(max_length=300)
    date_created = models.DateField()

    def __str__(self):
        return self.recipe_name

    objects = models.Manager()


