from django.db import models

# Create your models here.
TYPE_CHOICES = [
    ('yes', 'yes'),
    ('no', 'no'),
]

class Resource(models.Model):
    name = models.CharField(max_length=60)
    URL = models.CharField(max_length=60, default='', null=False)
    free_version = models.CharField(max_length=50, choices=TYPE_CHOICES)
    key_features = models.TextField(max_length=200)

    objects = models.Manager()

    def __str__(self):
        return self.name