from django.db import models

# Create your models here.


TYPE_CHOICES = (
    ('Darth Vader', 'Darth Vader'),
    ('Luke Skywalker', 'Luke Skywalker'),
    ('Obi-Wan Kenobi', 'Obi_Wan Kenobi'),
    ('Kylo Ren', 'Kylo Ren'),
)

class TheForce(models.Model):
    Jedi = models.CharField(max_length=25, choices=TYPE_CHOICES)
    Your_Name = models.CharField(max_length=25, default="", blank=True, null=False)
    Your_favorite_movie = models.CharField(max_length=25, default="", blank=True, null=False)
    Your_Favorite_Scene = models.CharField(max_length=25, default="", blank=True, null=False)
    Light_or_Dark = models.CharField(max_length=25, default="", blank=True, null=True)
    Is_The_Force_With_You = models.TextField(max_length=500, default="", blank=True)

    objects = models.Manager()