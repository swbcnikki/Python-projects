from django.db import models

# Dictionary
TYPE_CHOICES = [
    ("Appetizers", "Appetizers"),
    ("Entrees", "Entrees"),
    ("Drinks", "Drinks"),
    ("Snacks", "Snacks"),
]


# When a recipe is created these are the fields of info that are filled out
class Recipe(models.Model):
    recipe_type = models.CharField(max_length=60, choices=TYPE_CHOICES)
    # blank=False does not allow for the forms on the webpage to be left blank
    # null=False does not allow for the it to be blank in the templates
    recipe_name = models.CharField(max_length=100, default="", blank=False, null=False)
    recipe_ingredients = models.TextField(default="Please write you're ingredients and amounts", blank=False)
    recipe_instructions = models.TextField(default='Please write your instructions here', blank=False)

    objects = models.Manager()

    def __str__(self):
        return self.recipe_name
