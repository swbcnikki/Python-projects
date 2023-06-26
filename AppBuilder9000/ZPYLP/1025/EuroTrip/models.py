from django.db import models

# The models I created required a lot of choice selections so for the next little bit here are the choices.
# The first field in the choices is what will be stored in the dB, the second field is what the user sees.


timeZoneChoices = (
    ('5', 'Finland, Ukraine, Romania, Greece'),
    ('6', 'Belarus, Western Russia, Turkey'),
    ('7', 'Georgia, Azerbaijan')
)

safetyChoices = (
    ('not safe, do not visit', 'Not safe at all'),
    ('not safe', 'Not safe, would not bring family'),
    ('somewhat safe', 'Decently safe, just be careful and wise'),
    ('safer than others', 'No safety threats, but there are areas I would not go'),
    ('Extremely Safe', 'Really safe, my grandma would be ok')
)

priceChoices = (
    ('dirt cheap', 'Extremely cheap to visit'),
    ('somewhat cheap', 'Not the cheapest, but close'),
    ('average price', 'Average price'),
    ('somewhat decadent', 'A little lavish'),
    ('very decadent', 'Only for the high rollers')
)

# I'm creating 3 basic models here to contain pertinent information about destinations in Europe


class Location(models.Model):
    country = models.CharField(max_length=200, help_text="Which country are we talking about?", null=True)
    city = models.CharField(max_length=200, help_text="Which city are we talking about?")
    timeZone = models.CharField(max_length=200, help_text="Please select from the list, to convert it's time zone.",
                                choices=timeZoneChoices)
    safety = models.CharField(max_length=200, help_text="Please choose a safety rating for this location.",
                              choices=safetyChoices)
    prices = models.CharField(max_length=150, help_text="Please consider the total price of the trip when rating",
                              choices=priceChoices)

    objects = models.Manager()

    def __str__(self):
        return self.city
