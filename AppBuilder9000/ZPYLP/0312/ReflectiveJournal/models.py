from django.db import models

MOOD_CHOICES = [
    ('Awesome', 'Awesome'),
    ('Good', 'Good'),
    ('Meh', 'Meh'),
    ('Down', 'Down'),
    ('Awful', 'Awful'),
]

SLEEP_CHOICES = [
    ('0-4 Hours','0-4 Hours'),
    ('5-6 Hours','5-6 Hours'),
    ('7-8 Hours','7-8 Hours'),
    ('9-10 Hours','9-10 Hours'),
    ('11-24 Hours','11-24 Hours'),
]

class Entry(models.Model):
    name = models.CharField(max_length=50, default='', blank=False, null=True)
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    Mood = models.CharField(max_length=50, default='', choices=MOOD_CHOICES, blank=False, null=True)
    Hours_Slept = models.CharField(max_length=50, default='', choices=SLEEP_CHOICES, blank=False, null=True)



    def __str__(self):
        return 'Entry #{}'.format(self.id)

    class Meta:
        verbose_name_plural = 'Entries'

