from django.db import models


class Recipes(models.Model):
    recipe_name = models.CharField(default='Enter recipe name', max_length=30)
    recipe_description = models.TextField(default='Enter a brief description')
    cook_time = models.IntegerField(default='60')
    ingredients = models.TextField(default='list, ingredients, separated, by, commas')
    instructions = models.TextField(default='1.\n\n2.\n\n3.')
    Recipe = models.Manager()

    def __str__(self):
        return self.recipe_name
