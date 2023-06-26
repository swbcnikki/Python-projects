from django.db import models

ACCOMMODATION_CHOICE = (
    ('Coach Seat', 'Coach Seat'),
    ('Roomette', 'Roomette'),
    ('Bedroom', 'Bedroom'),
    ('Bedroom Suite', 'Bedroom Suite'),
    ('Family Bedroom', 'Family Bedroom'),
    ('Accessible Bedroom', 'Accessible Bedroom'),
)

EB_STATES = (
    ('Illinois', 'Illinois'),
    ('Washington', 'Washington'),
    ('Oregon', 'Oregon'),
)

EB_LONG = (
    ('Chicago', 'Chicago'),
    ('Seattle', 'Seattle'),
    ('Portland', 'Portland'),
)

EB_SHORT = (
    ('Glenview', 'Glenview'),
    ('Everett', 'Everett'),
    ('none', 'none'),
)

# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=25, default='first', blank=True, null=False)
    last_name = models.CharField(max_length=25, default='last', blank=True, null=False)
    email = models.EmailField(max_length=25, default='email', blank=True, null=False)
    phone = models.CharField(max_length=15, default='optional', blank=True, null=False)
    travelDate = models.DateField(blank=False)
    accommodation = models.CharField(max_length=20, default='', blank=False, null=False, choices=ACCOMMODATION_CHOICE)
    guests = models.IntegerField(default=00, blank=True, null=False)


    objects = models.Manager()

    def __str__(self):
        return self.phone

