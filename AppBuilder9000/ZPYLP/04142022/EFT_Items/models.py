from django.db import models

# Create your models here.
ITEM_TYPE_CHOICES = (
    ('Barter', 'Barter'),
    ('Keys', 'Keys'),
    ('Gear', 'Gear'),
    ('Weapons', 'Weapons'),
    ('Provisions', 'Provisions'),
    ('Meds', 'Meds'),
    ('Others', 'Others'),
)

FOUND_IN_RAID_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)


class EFTItems(models.Model):
    type = models.CharField(max_length=30, choices=ITEM_TYPE_CHOICES)
    name = models.CharField(max_length=100)
    amount_required = models.IntegerField(blank=True, null=True)
    hideout = models.CharField(max_length=100, blank=True)
    quest = models.CharField(max_length=100, blank=True)
    found_in_raid = models.CharField(max_length=5, default="", blank=True, choices=FOUND_IN_RAID_CHOICES)

    # Create objects manager to access database
    objects = models.Manager()

    def __str__(self):
        return self.name
