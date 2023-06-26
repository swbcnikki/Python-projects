from django.db import models

THREAT = [  # establish threat levels
    ('Nonexistent', 'Nonexistent'),
    ('Mild Inconvenience', 'Mild Inconvenience'),
    ('Minor Threat', 'Minor Threat'),
    ('Robin Equivalent', 'Robin Equivalent'),
    ('Major Threat', 'Major Threat'),
    ('World Ending', 'World Ending'),
]


# set up the Heroes class for the db.
class Heroes(models.Model):
    alias = models.CharField(max_length=30, default="", blank=False, null=False)
    secret_Identity = models.CharField(max_length=50, default="", blank=True, null=False)
    ability_Name = models.CharField(max_length=25, default="", blank=False, null=False)
    ability_Summary = models.TextField(max_length=200, default="", blank=False, null=False)
    weakness = models.CharField(max_length=25, default="", blank=True, null=False)
    threat_Level = models.CharField(max_length=20, default="", choices=THREAT)

    # assign a manager
    heroes = models.Manager()

    def __str__(self):
        return self.alias
