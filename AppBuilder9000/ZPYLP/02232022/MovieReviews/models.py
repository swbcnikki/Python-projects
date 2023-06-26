from django.db import models


# Created Star Choices
TYPE_CHOICES = [
    ('1 star', '1 star'),
    ('2 stars', '2 stars'),
    ('3 stars', '3 stars'),
    ('4 stars', '4 stars'),
    ('5 stars', '5 stars'),
]

# The models for the entries in the database


class Movies(models.Model):
    genre = models.CharField(max_length=100, default="", blank=True)
    title = models.CharField(max_length=300, default="", blank=True, null=False)
    description = models.TextField(max_length=1000, default="", blank=True)
    rating = models.CharField(max_length=50, default="", blank=True)
    director = models.CharField(max_length=100, default="", blank=True)
    actor = models.CharField(max_length=100, default="", blank=True)
    stars = models.CharField(max_length=100, choices=TYPE_CHOICES)

    Movies = models.Manager()

    def __str__(self):
        return self.title






