from django.db import models

# Create your models here.

TYPE_CHOICES = (
    ('pre-mix', 'pre-mix'),
    ('post-mix/pre-master', 'post-mix/pre-master'),
    ('post-master', 'post-master'),

)

class Files(models.Model):
    type = models.CharField(max_length=60, choices=TYPE_CHOICES)
    name = models.CharField(max_length=50, default="", blank=True, null=False)
    genre = models.CharField(max_length=50, default="", blank=True, null=False)


    objects = models.Manager()

def __str__(self):
    return self.name
