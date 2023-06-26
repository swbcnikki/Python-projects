from django.db import models

TRACK_ME = [
    ('startTracking', 'startTracking'),
    ('dontTrack', 'dontTrack'),
]
CHOICES = [
    ('yes', 'yes'),
    ('no', 'no'),
]

class Location(models.Model):
    location_name = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

class User(models.Model):
     firstName = models.CharField(max_length=50)
     lastName = models.CharField(max_length=50)
     description = models.CharField(max_length=100)







def __str__(self):
    return self.TrackMe