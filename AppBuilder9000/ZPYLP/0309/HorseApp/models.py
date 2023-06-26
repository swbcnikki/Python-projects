from django.db import models

# Create your models here.

# selectable choices for racehorse model


AGE_CHOICES = [
    ('two year olds', 'two year olds'),
    ('three year olds', 'three year olds'),
    ('four year olds and up', 'four year olds and up'),
]

GENDER_CHOICES = [
    ('male', 'male'),
    ('female', 'female')
]


class RaceHorse(models.Model):
    horse_name = models.CharField(max_length=100, default="", blank=True, null=False)
    age = models.CharField(max_length=60, default="", blank=True, null=False, choices=AGE_CHOICES)
    gender = models.CharField(max_length=10, default="", blank=True, null=False, choices=GENDER_CHOICES)
    color = models.CharField(max_length=10, default="", blank=True, null=False)
    sire = models.CharField(max_length=100, default="unknown", blank=True, null=False)
    dam = models.CharField(max_length=100, default="unknown", blank=True, null=False)
    speed_figure = models.IntegerField(default=0,null=False)


    RaceHorses = models.Manager()

    def __str__(self):
        return self.horse_name


# plan to add race model with surface and location fields
