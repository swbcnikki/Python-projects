from django.db import models


# tuple choices for database options of object size.
SIZE_CHOICE = [
    ('Regular', '4_inch'),
    ('Medium', '6_inch'),
    ('Jumbo', '10_inch'),
]
# tuple choices for database option of object rarity
CHASE = [
    ('Y', 'yes'),
    ('N', 'no'),
]

# class model setting up the database to keep track of pop information inputted into the collection database
class FunkoPopName(models.Model):
    size = models.CharField(max_length=7, choices=SIZE_CHOICE)
    name = models.CharField('Name', max_length=40)
    fandome = models.CharField(max_length=60)
    chase = models.CharField('Chase', max_length=3, choices=CHASE)
    purchase_price = models.DecimalField(max_digits=6, decimal_places=2)
    value = models.DecimalField(max_digits=6, decimal_places=2)

    objects = models.Manager()

    def __str__(self):
        return self.name

