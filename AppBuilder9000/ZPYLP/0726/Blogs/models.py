from django.db import models


MOOD_CHOICES = [
    ('Awesome', 'Awesome'),
    ('Good', 'Good'),
    ('Meh', 'Meh'),
    ('Down', 'Down'),
    ('Awful', 'Awful'),
    ('Destructive', 'Destructive'),
]

class Entry(models.Model):
    name = models.CharField(max_length=50, default='', blank=False, null=True)
    text = models.TextField(default='')
    date_posted = models.DateTimeField(default='')
    Mood = models.CharField(max_length=50, default='', choices=MOOD_CHOICES, blank=False, null=True)




    def __str__(self):
        return 'Entry #{}'.format(self.id)

    class Meta:
        verbose_name_plural = 'Entries'

