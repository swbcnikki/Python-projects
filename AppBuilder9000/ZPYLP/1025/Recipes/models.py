from django.db import models

# Create your models here.

TYPE_CHOICES = (
    ('Breakfast','Breakfast'),
    ('Lunch','Lunch'),
    ('Dinner','Dinner'),
    ('Dessert','Dessert'),
)


class Recipe(models.Model):
    type = models.CharField(max_length=9, choices=TYPE_CHOICES)
    user_name = models.CharField(max_length=24, default="", blank=True, null=False)
    recipe_name = models.CharField(max_length=24, default="", blank=True, null=False)
    main_ingredient = models.CharField(max_length=14, default="", blank=True, null=False)
    main_ingredient_2 = models.CharField(max_length=14, default="", blank=True, null=True)
    steps = models.TextField(max_length=400, default="", blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.recipe_name