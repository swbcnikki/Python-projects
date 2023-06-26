from django.db import models

Choice_DropDown = [
    ('Snack', 'Snack'),
    ('Breakfast', 'Breakfast'),
    ('Lunch', 'Lunch'),
    ('Dinner', 'Dinner'),
    ('Sunday Meal', 'Sunday Meal'),
    ('Sweets', 'Sweets'),
]

# Recipe class model
# This is the basic model for the database.#


class Recipes(models.Model):
    category = models.CharField(max_length=20, choices=Choice_DropDown, default='Pick from the dropdown!')
    name = models.CharField(default='What did Grandma Call it?', max_length=40)
    prep_time = models.CharField(max_length=30, default='60 minutes')
    grandma_story = models.TextField(default='Recall a time you made this with Grandma! Tell everyone about it... ')
    ingredients = models.TextField(default='list, ingredients, separated, by, commas')
    instructions = models.TextField(default='Remember How Grandma Used to Do it? Tell about it!')

    def __str__(self):
        return self.name

    Recipes = models.Manager()



