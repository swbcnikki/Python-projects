from django.db import models
#for review class
INTEGER_CHOICES = [tuple([x, x]) for x in range(1, 11)]
POP_CHOICES = [('Family', 'Family'), ('Young Professional', 'Young Professional'), ('Retiree', 'Retiree')]
COMMUTE_CHOICES = [('Long', 'Long'), ('Fair', 'Fair'), ('Short', 'Short')]
WALK_CHOICES = [('Very Walkable', 'Very Walkable'), ('Somewhat Walkable', 'Somewhat Walkable'), ('Not Walkable', 'Not Walkable')]



#for neighborhood class

LOCATION_CHOICES = [('Northwest', 'Northwest'), ('North', 'North'), ('Northeast', 'Northeast'), ('Southeast', 'Southeast'),
                    ('Southwest', 'Southwest'), ('Beaverton', 'Beaverton'), ('Hillsboro', 'Hillsboro')]


class Neighborhood(models.Model):
    name = models.CharField(max_length=75, unique=True, default="")
    location = models.CharField(choices=LOCATION_CHOICES,max_length=50)

    def __str__(self):
        return self.name + " Location: " + self.location


class Review(models.Model):
    date = models.DateField()
    rating = models.IntegerField(choices=INTEGER_CHOICES)
    commute = models.CharField(max_length=40, choices=COMMUTE_CHOICES)
    walkability = models.CharField(max_length=40, choices=WALK_CHOICES)
    reviewer_life_stage = models.CharField(max_length=40, choices=POP_CHOICES)
    comment = models.CharField(max_length=750)
    neighborhood_id = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)

    Reviews = models.Manager()

