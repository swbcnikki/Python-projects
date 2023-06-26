from django.db import models
from django import forms

Sports_Teams = (
    ('dallas cowboys', 'Dallas Cowboys'),
    ('dallas mavericks', 'Dallas Mavericks'),
    ('texas rangers', 'Texas Rangers'),
    ('dallas stars', 'Dallas Stars'),
    ('dallas wings', 'Dallas Wings'),
    ('fc dallas', 'FC Dallas'),
)


class Dallas(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    fav_sports_team = models.CharField(max_length=50, choices=Sports_Teams, default='Dallas Cowboys')
    fav_activity = models.TextField(max_length=150, default='')

    Dallas = models.Manager()

    def __str__(self):
        return self.first_name + '' + self.last_name

