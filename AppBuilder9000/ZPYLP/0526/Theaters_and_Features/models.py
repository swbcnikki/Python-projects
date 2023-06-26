from django.db import models

MOVIE_TYPES = [
    ('First Run', 'First Run'),
    ('Previously Released', 'Previously Released'),
    ('Independent', 'Independent'),
]

SEAT_TYPES = [
    ('Stadium', 'Stadium'),
    ('Deluxe Reclinable', 'Deluxe Reclinable'),
    ('Couches', 'Couches'),
    ('Other', 'Other'),
]

HAS_ALCOHOL = [
    ('No Alcohol', 'No Alcohol'),
    ('Full Bar', 'Full Bar'),
    ('Beer', 'Beer'),
    ('Wine', 'Wine'),
    ('Beer and Wine', 'Beer and Wine'),
    ('Liquor', 'Liquor'),
]

FOOD_TYPES = [
    ('Popcorn and Candy', 'Popcorn and Candy'),
    ('Pizza and Snacks', 'Pizza and Snacks'),
    ('Full Menu', 'Full Menu'),
]

class Theaters(models.Model):
    Name = models.CharField(max_length=40)
    Address = models.CharField(max_length=80)
    Phone = models.IntegerField()
    MovieType = models.CharField(max_length=20, choices=MOVIE_TYPES)
    SeatType = models.CharField(max_length=20, choices=SEAT_TYPES)
    HasAlcohol = models.CharField(max_length=20, choices=HAS_ALCOHOL)
    Food = models.CharField(max_length=20, choices=FOOD_TYPES)

    objects = models.Manager()

    def __str__(self):
        return self.Name
