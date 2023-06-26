from django.db import models

type_choices = [
    ('Campsites', 'Campsites'),
    ('RVs', 'RVs'),
    ('Both', 'Both'),
]

amenities_choices = [
    ('Pets Allow', 'Pets Allow'),
    ('Toilets', 'Toilets'),
    ('Campfires', 'Campfires'),
    ('Water', 'Water'),
    ('Showers', 'Showers'),
    ('Picnic Tables', 'Picnic Tables'),
    ('Wifi', 'Wifi'),
]

activities_choices = [
    ('Hiking', 'Hiking'),
    ('Swimming', 'Swimming'),
    ('Fishing', 'Fishing'),
    ('Biking', 'Biking'),
    ('Off-Roading', 'Off-Roading'),
    ('Wildlife Watching', 'Wildlife Watching'),
]


class CampSites(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=60, choices=type_choices)
    site_amenities = models.CharField(max_length=60, default="", choices=amenities_choices)
    site_activities = models.CharField(max_length=60, default="", choices=activities_choices)
    description = models.TextField(max_length=500, default="", blank=True)
    city = models.CharField(max_length=500, default="", blank=True)
    state = models.CharField(max_length=500, default="", blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.name
