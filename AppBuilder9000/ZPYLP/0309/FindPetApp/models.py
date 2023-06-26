from django.db import models
from datetime import datetime

# Create your models here.

AnimalType = [('Dog', 'Dog'), ('Cat', 'Cat')]
States = [
    ("AL", "AL"),
    ("AK", "AK"),
    ("AZ", "AZ"),
    ("AR", "AR"),
    ("CA", "CA"),
    ("CO", "CO"),
    ("CT", "CT"),
    ("DE", "DE"),
    ("FL", "FL"),
    ("GA", "GA"),
    ("HI", "HI"),
    ("ID", "ID"),
    ("IL", "IL"),
    ("IN", "IN"),
    ("IA", "IA"),
    ("KS", "KS"),
    ("KY", "KY"),
    ("LA", "LA"),
    ("ME", "ME"),
    ("MD", "MD"),
    ("MA", "MA"),
    ("MI", "MI"),
    ("MN", "MN"),
    ("MS", "MS"),
    ("MO", "MO"),
    ("MT", "MT"),
    ("NE", "NE"),
    ("NV", "NV"),
    ("NH", "NH"),
    ("NJ", "NJ"),
    ("NM", "NM"),
    ("NY", "NY"),
    ("NC", "NC"),
    ("ND", "ND"),
    ("OH", "OH"),
    ("OK", "OK"),
    ("OR", "OR"),
    ("PA", "PA"),
    ("RI", "RI"),
    ("SC", "SC"),
    ("SD", "SD"),
    ("TN", "TN"),
    ("TX", "TX"),
    ("UT", "UT"),
    ("VT", "VT"),
    ("VA", "VA"),
    ("WA", "WA"),
    ("WV", "WV"),
    ("WI", "WI"),
    ("WY", "WY"),
]


class AvailablePet(models.Model):
    name = models.CharField(max_length=35, blank=False)
    age = models.CharField(max_length=35, default='', blank=True)
    birthday = models.DateField()
    breed = models.CharField(max_length=25, blank=False)
    color = models.CharField(max_length=25, blank=False)
    animal = models.CharField(max_length=10, choices=AnimalType)
    description = models.CharField(max_length=500, help_text="Describe the wonderful animal here!")
    location = models.CharField(max_length=10, choices=States)
    email = models.EmailField(max_length=40, default="")

    Available = models.Manager()

    def __str__(self):
        return self.name + " the " + self.breed


class PetApplicant(models.Model):
    first_name = models.CharField(max_length=35, blank=False)
    last_name = models.CharField(max_length=35, blank=False)
    preference = models.CharField(max_length=10, choices=AnimalType)
    state = models.CharField(max_length=10, choices=States)
    contact = models.EmailField(max_length=40, default="")

    Applicant = models.Manager()

    def __str__(self):
        return self.first_name + " " + self.last_name
