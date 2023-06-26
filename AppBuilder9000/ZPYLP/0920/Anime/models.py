from django.db import models


TYPE_CHOICES = [
    ('supernatural', 'supernatural'),
    ('action', 'action'),
    ('sports', 'sports'),
    ('life', 'life'),
]


class Description(models.Model):
    name = models.CharField(max_length=60)
    anime = models.CharField(max_length=60, default='', null=False)
    release = models.CharField(max_length=60)
    genre = models.CharField(max_length=50, choices=TYPE_CHOICES)
    episodes = models.CharField(max_length=200)

    objects = models.Manager()

    def __str__(self):
        return self.name
