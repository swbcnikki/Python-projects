from django.db import models


TYPE_CHOICES = [
    ('legs', 'legs'),
    ('back', 'back'),
    ('chest', 'chest'),
    ('arms', 'arms'),
    ('core', 'core'),
]


class Moves(models.Model):
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    name = models.CharField(max_length=50, default="", blank=True, null=False)
    description = models.TextField(max_length=500, default="", blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.name
