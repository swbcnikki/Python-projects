from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
class Publishers(models.Model):
    name = models.CharField(max_length=50)

    Publisher = models.Manager()

    def __str__(self):
        return self.name

GENRES = [
    ('action', 'action'),
    ('racing', 'racing'),
    ('horror', 'horror'),
    ('adventure', 'adventure'),
    ('RPG', 'RPG'),
    ('RTS', 'RTS'),
]


class Games(models.Model):
    name = models.CharField(max_length=50)
    release_year = models.IntegerField(validators=[
        MinValueValidator(1960),
        MaxValueValidator(2025)
    ])
    rating = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(100)
    ], default=50)
    genre = models.CharField(max_length=50, choices=GENRES, default=GENRES[0])
    publisher_name = models.CharField(max_length=50)
    publisher = models.ForeignKey(Publishers, on_delete=models.CASCADE, default='', blank=True, null=True)
    review = models.TextField(max_length=500, default='', blank=True)

    Game = models.Manager()


    def __str__(self):
        return self.name


class FavoriteGame(models.Model):
    name = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(100)
    ])
    # this should be a charfield and not a datefield due to how the data is collected
    release_date = models.CharField(max_length=50)

    Favorites = models.Manager()

    def __str__(self):
        return self.name