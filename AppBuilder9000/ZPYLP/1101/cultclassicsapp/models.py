from django.db import models

# Create your models here.

TYPE_CHOICES = (
    ('Genres', 'Genres'),
    ('Year', 'Year'),
    ('Director', 'Director'),
    ('Color', 'Color'),
)

class CultClassics(models.Model):
    type = models.CharField(max_length=25, choices=TYPE_CHOICES)
    user_name = models.CharField(max_length=25, default="", blank=True, null=False)
    Movie_Title = models.CharField(max_length=25, default="", blank=True, null=False)
    Actor = models.CharField(max_length=25, default="", blank=True, null=False)
    Actress = models.CharField(max_length=25, default="", blank=True, null=True)
    Description = models.TextField(max_length=500, default="", blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.Movie_Title



