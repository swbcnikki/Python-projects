from django.db import models

tagOption = [
    ('Programming', 'Programming'),
    ('Strategy', 'Strategy'),
    ('Algorithms', 'Algorithms'),
]

class Story(models.Model):
    title = models.CharField(max_length=10, blank=True)
    first_name = models.CharField(max_length=10, blank=True)
    last_name = models.CharField(max_length=10, blank=True)
    article = models.TextField(max_length=1000, blank=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    tags = models.CharField(max_length=50, blank=True, choices=tagOption)

    Stories = models.Manager()

    def __str__(self):
        return self.fName + " " + self.lName


class Resource(models.Model):
    title = models.CharField(max_length=10, blank=True)
    subtitle = models.CharField(max_length=10, blank=True)
    objective = models.TextField(max_length=1000, blank=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    content = models.TextField(max_length=1000, blank=True)
    URL = models.URLField(max_length=200, blank=True)

    Resources = models.Manager()

