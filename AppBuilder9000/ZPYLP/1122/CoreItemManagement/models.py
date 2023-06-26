from django.db import models


"""
Categories:
- Produce
- Tobacco
- Vehicle
"""


CATEGORY = [
    ('Other', 'Other'),
    ('Produce', 'Produce'),
    ('Tobacco', 'Tobacco'),
    ('Vehicle', 'Vehicle'),
]


# Create your models here.
class Item(models.Model):
    id = models.AutoField(primary_key=True)
    item_pn = models.IntegerField()
    item_name = models.CharField(max_length=30)
    item_count = models.IntegerField()
    item_category = models.CharField(max_length=60, choices=CATEGORY)
    item_price = models.DecimalField(max_digits=7, decimal_places=2)
    # Vendor foreign key here
    item_vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE, default=None)


"""

"""


class Vendor(models.Model):
    id = models.AutoField(primary_key=True)
    vendor_name = models.CharField(max_length=30)
    vendor_number = models.IntegerField()
    vendor_category = models.CharField(max_length=60, choices=CATEGORY, default=0)
    vendor_contact = models.IntegerField()

