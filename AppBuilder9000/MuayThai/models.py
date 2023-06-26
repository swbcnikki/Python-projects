from django.db import models

# Dropdown menu
WeightClass_Dropdown = [
    ('Flyweight', 'Flyweight'),
    ('Bantamweight', 'Bantamweight'),
    ('Featherweight', 'Featherweight'),
    ('Welterweight', 'Welterweight'),
    ('Middleweight', 'Middleweight'),
    ('Heavyweight', 'Heavyweight'),
]

# weight class dropdown
# basic model for database
class Fighter(models.Model):
    category = models.CharField(max_length=60, choices=WeightClass_Dropdown, default='Choose your weight class!')
    first_name = models.CharField(max_length=50, default="", blank=True, null=False)
    last_name = models.CharField(max_length=50, default="", blank=True, null=False)
    country = models.CharField(max_length=60, default="", blank=True, null=False)
    weight_in_lbs = models.CharField(max_length=20, default="", blank=True, null=False)
    gym = models.CharField(max_length=60, default="", blank=True, null=False)

    Fighter = models.Manager()

    def __str__(self):
        return self.first_name + '' + self.last_name



