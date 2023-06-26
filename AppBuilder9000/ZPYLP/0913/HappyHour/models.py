from django.db import models

# Create your models here.



HIGHLIGHT_CHOICES =  (
    ('good food','good food'),
    ('good drinks','good drinks'),
    ('stiff pour','stiff pour'),
    ('budget friendly','budget friendly'),
    ('late night HH','late night HH'),
    ('dietary options','dietary options'),
    ('ambiance','ambiance'),
    ('location','location'),
)

STARS = (
    ('one star','one star'),
    ('two star','two star'),
    ('three star','three star'),
    ('four star','four star'),
    ('five star','five star'),
)

class Restaurants(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    highlights = models.CharField(max_length=50, choices=HIGHLIGHT_CHOICES)
    review = models.TextField(max_length= 500, blank= True)
    rating = models.CharField(max_length=50, choices= STARS)
    image = models.CharField(max_length=300, default='', blank=True)

    objects = models.Manager()

    # as the name not the primary key
    def __str__(self):
        return self.name


