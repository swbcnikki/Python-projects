from django.db import models

type_choices = [
    ('Outdoor', 'Outdoor'),
    ('Indoor', 'Indoor'),
    ('Both', 'Both'),
]

bathingsuit_choices = [
    ('Required', 'Required'),
    ('Optional', 'Optional'),
]

stay_overnight = [
    ('Tent Camping', 'Tent Camping'),
    ('Trailer Hookups', 'Trailer Hookups'),
    ('Cabin Rentals', 'Cabin Rentals'),
    ('Resort', 'Resort'),
    ('Camping & Rentals', 'Camping & Rentals'),
    ('No Overnight Stay', 'No Overnight Stay'),
]

class HotSprings(models.Model):
    hot_springs_name = models.CharField(max_length=50)
    hot_springs_type = models.CharField(max_length=60, choices=type_choices)
    clothing_optional = models.CharField(max_length=60, choices=bathingsuit_choices)
    stay_accommodations = models.CharField(max_length=60, default="", choices=stay_overnight)
    description = models.TextField(max_length=500, default="", blank=True)


class Location(HotSprings):
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    objects = models.Manager()

    def __str__(self):
        return self.hot_springs_name


