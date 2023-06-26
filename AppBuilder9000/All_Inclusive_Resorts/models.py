from django.db import models

# Create your models here.
Resort_Rating = [
    ('1 Star', '1 Star'),
    ('2 Stars', '2 Stars'),
    ('3 Stars', '3 Stars'),
    ('4 Stars', '4 Stars'),
    ('5 Stars', '5 Stars'),
]

Resort_Type = [
    ('Adult-Only', 'Adult-Only'),
    ('Family', 'Family'),

]
# Initiating model


class ResortListings(models.Model):
    resort_name = models.CharField(max_length=100, null=False)
    resort_type = models.CharField(max_length=50, choices=Resort_Type)
    resort_country = models.CharField(max_length=100, null=False)
    resort_rating = models.CharField(max_length=20, choices=Resort_Rating)
    resort_description = models.CharField(max_length=500, null=False)

    Resorts = models.Manager()

    def __str__(self):
        return self.resort_name


class ResortTraveler(models.Model):
    traveler_name = models.CharField(max_length=100, null=False)
    traveler_party_size = models.CharField(max_length=2)
    traveler_resort = models.CharField(max_length=100, null=False)
    traveler_contact = models.CharField(max_length=50, null=False)

    ResortTraveler = models.Manager

    def __str__(self):
        return self.traveler_name



