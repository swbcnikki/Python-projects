from django.db import models

# Adding a tuple of choices for the interest level integer field
InterestLevelChoices = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)


# Create your models here.
# A very basic model taking in the five parameters we discussed on the home page template!
class SteamInterestAppBase(models.Model):
    game_title = models.CharField(max_length=30)
    genre = models.CharField(max_length=20)
    date_released = models.DateTimeField()
    date_purchased = models.DateTimeField()
    interest_level = models.IntegerField(choices=InterestLevelChoices)

    objects = models.Manager()

    # An easy way to see what game we're talking about when analyzing the templates
    def __str__(self):
        return self.game_title