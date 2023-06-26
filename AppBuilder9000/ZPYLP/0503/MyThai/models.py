from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

DISH_TYPES = [
    ('Curry', 'Curry'),
    ('Noodles', 'Noodles'),
    ('Soup', 'Soup'),
    ('Appetizers', 'Appetizers'),
    ('Other', 'Other'),
]


class Restaurant(models.Model):
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=13, default='(000)000-0000')
    address = models.CharField(max_length=95)
    city = models.CharField(max_length=15, default='Portland')
    rating = models.IntegerField(
        validators=[MaxValueValidator(10), MinValueValidator(0)]  # Check to make sure rating in range.
    )

    objects = models.Manager()

    def __str__(self):
        return self.name


class Dish(models.Model):
    dishName = models.CharField(max_length=40)
    dishType = models.CharField(max_length=10, choices=DISH_TYPES)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[MaxValueValidator(10), MinValueValidator(0)]  # Check to make sure rating in range.
    )
    description = models.CharField(max_length=255)

    objects = models.Manager()

    def __str__(self):
        return self.dishName
