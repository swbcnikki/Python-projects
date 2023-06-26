from django.db import models

ITEM_TYPE_CHOICES = [
    ('Materials', 'Materials'),
    ('Tools', 'Tools'),
    ('Weapons', 'Weapons'),
    ('Armor', 'Armor'),
]


class Item(models.Model):
    item_type = models.CharField(max_length=20, choices=ITEM_TYPE_CHOICES)
    item_name = models.CharField(max_length=50)
    item_level = models.IntegerField()
    item_description = models.TextField(max_length=1000, default="Item Description")

    item_object = models.Manager()

    def __str__(self):
        return self.item_name

