from django.db import models

Drink_Type = [
    ('hot drinks', 'hot drinks'),
    ('cold drinks', 'cold drinks'),
    ('breakfast', 'breakfast'),
    ('extras', 'extras'),

]


# Drinks are the drink types, name of drinks, description, and so forth
class Drink(models.Model):
    type = models.CharField(max_length=60, choices=Drink_Type)
    name = models.CharField(max_length=60, default="", blank=True, null=False)
    description = models.TextField(max_length=300, default="", blank=True)
    price = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

    object = models.Manager()

    def __str__(self):
        return self.name


class Recipe(models.Model):
    type = models.CharField(max_length=60, choices=Drink_Type)
    name = models.CharField(max_length=60, default="", blank=True, null=False)
    recipe = models.TextField(max_length=10000)
    duration = models.IntegerField()

    recipes = models.Manager()

    def __str__(self):
        return self.name
