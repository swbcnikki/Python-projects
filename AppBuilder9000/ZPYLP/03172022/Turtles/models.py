from django.db import models

# Defining a new tuple object(species of turtles)
TYPE_CHOICES = [
    ('Turtle', 'Turtle'),
    ('Tortoise', 'Tortoise'),
    ('Terrapin', 'Terrapin')
]

# Defining a new tuple object(native region of turtles)
LOCALITY_CHOICES = [
    ('Americas', 'Americas'),
    ('Europe', 'Europe'),
    ('Asia', 'Asia')
]


# Creating my model
class Turtles(models.Model):
    name = models.CharField(max_length=30)
    species = models.CharField(max_length=15, choices=TYPE_CHOICES)
    description = models.TextField(max_length=150)
    rescue_cost = models.DecimalField(max_digits=1000, decimal_places=2)
    locality = models.CharField(max_length=15, choices=LOCALITY_CHOICES)

    # Objects manager
    Turtles = models.Manager()

    # Using dunder method to reference 'Turtles' class
    def __str__(self):
        return self.name
