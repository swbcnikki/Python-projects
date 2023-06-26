from django.db import models

SIDE = [
    ('Alliance', 'Alliance'),
    ('Horde', 'Horde'),
    ('Neutral', 'Neutral'),
]

PERSON = [
    ('Thrall', 'Thrall'),
    ('Jaina', 'Jaina'),
    ('Anduin', 'Anduin'),
    ('Cairne Bloodhoof', 'Cairne Bloodhoof'),
    ('Tyrande Whisperwind', 'Tyrande Whisperwind'),
    ('Other', 'Other'),
]

CHOICE = [
    ('Dark', 'Dark'),
    ('Light', 'Light'),
]

class Character(models.Model):
    name = models.CharField(verbose_name='Character name', max_length=100, choices=PERSON, default='')
    side = models.CharField(verbose_name='What side are they for the horde, alliance, or neutral?', max_length=50, choices=SIDE, default='')
    choice = models.CharField(verbose_name='Are they for dark side or light side?', max_length=100, choices=CHOICE, default='')
    powers = models.CharField(verbose_name='Powers', max_length=50, blank=False, null=False)
    bio = models.TextField(verbose_name='Biography', blank=False, null=False)

    object = models.Manager()

    def __str__(self):
        return self.name

class Favorite(models.Model):
    name = models.CharField(verbose_name='Character name', max_length=100, default="", blank=True, null=False)
    description = models.CharField(verbose_name='Description', max_length=500, default="", blank=True)
    path = models.CharField(verbose_name='Path', max_length=100)
    extension = models.CharField(verbose_name='Extension', max_length=50,
                                default='')
    api_id = models.CharField(verbose_name='ID', max_length=50,
                                      default='', blank=False)
    link = models.CharField(verbose_name='Link', max_length=150, default=True, blank=True)

    object = models.Manager()

    def __str__(self):
        return self.name
