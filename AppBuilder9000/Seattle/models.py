from django.db import models

Place_Type = [
    ('Food', 'Food'),
    ('Hotel', 'Hotel'),
    ('Parking', 'Parking'),
    ('Parks', 'Parks'),
    ('Attraction', 'Attraction')
]

class Places(models.Model):
    Category = models.CharField(max_length=50, choices=Place_Type, default='')
    Place = models.CharField(max_length=20, default='', blank=True, null=False)
    Description = models.CharField(max_length=500, default='', blank=True, null=False)

    PlacesManager = models.Manager()

    def __str__(self):
        return self.place
