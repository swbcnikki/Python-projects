from django.db import models

# Create your models here.
TYPE_RACES = [
    ('Orc', 'Orc'),
    ('Troll', 'Troll'),
    ('Undead', 'Undead'),
    ('Blood Elf', 'Blood Elf'),
    ('Human', 'Human'),
    ('Night Elf', 'Night Elf'),
    ('Gnome', 'Gnome'),
    ('Dranei', 'Dranei'),
]

TYPE_GENDER = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]


class Character_create(models.Model):
    name = models.CharField(max_length=60)
    race = models.CharField(max_length=60, choices=TYPE_RACES)
    sex = models.CharField(max_length=60, choices=TYPE_GENDER)
    backstory = models.TextField(max_length=300, default="", blank=True)
    date_created = models.DateField()

    def __str__(self):
        return self.name

    objects = models.Manager()
