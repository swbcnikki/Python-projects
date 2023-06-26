from django.db import models


# Create motorcycle types
TYPE_MOTORCYCLE = (
    ('Sport', 'Sport'),
    ('Cruiser', 'Cruiser'),
    ('Touring', 'Touring'),
    ('Adventure', 'Adventure'),
    ('Standard', 'Standard')
)

# Motorcycle brands to choose
BRAND_MOTORCYCLE = (
    ('BMW', 'BMW'),
    ('Harley Davidson', 'Harley Davidson'),
    ('Kawasaki', 'Kawasaki'),
    ('Honda', 'Honda'),
    ('Yamaha', 'Yamaha'),
    ('Triumph', 'Triumph'),
    ('Ducati', 'Ducati'),
    ('Indian', 'Indian'),
    ('Victory', 'Victory'),
    ('KTM', 'KTM')
)

Rating_CHOICES = (
    (1, 'Poor'),
    (2, 'Average'),
    (3, 'Good'),
    (4, 'Very Good'),
    (5, 'Excellent')
)


class Route(models.Model):
    START_DESTINATION = models.CharField(max_length=50, default='')
    END_DESTINATION = models.CharField(max_length=50, default='')
    RATING = models.IntegerField(choices=Rating_CHOICES, default=1)

    def __str__(self):
        return self.START_DESTINATION

    objects = models.Manager()





class Motorcycle(models.Model):
    TYPE_MOTORCYCLE = models.CharField(max_length=20, default='', blank=True, null=False, choices=TYPE_MOTORCYCLE)
    BRAND_MOTORCYCLE = models.CharField(max_length=20, default='', blank=True, null=False, choices=BRAND_MOTORCYCLE)
    ENGINE_SIZE = models.CharField(max_length=10, default='', blank=True, null=False)
    MODEL_TYPE = models.CharField(max_length=30, default='', blank=True, null=True)
    RATING = models.IntegerField(choices=Rating_CHOICES, default=1)

    def __str__(self):
        return self.MODEL_TYPE

    objects = models.Manager()



