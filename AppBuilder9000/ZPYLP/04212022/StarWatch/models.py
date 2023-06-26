from django.db import models


CHOICES_objectType = (
    ('Moon', 'Moon'),
    ('Planet', 'Planet'),
    ('Star', 'Star'),
    ('Other', 'Other'),
    ('Unknown', 'Unknown'),
)


# Create your models here.
class celestialObjects(models.Model):
    object_name = models.CharField(default='Enter an object name', max_length=30)
    object_nickName = models.CharField(default='Enter an object nickname name', max_length=30)
    object_type = models.CharField(max_length=10, choices=CHOICES_objectType)
    object_description = models.TextField(default='Enter a description')
    object_brightness = models.IntegerField(default='0')
    object_direction = models.TextField(default='NNW')
    object_latitude = models.IntegerField(default='45')
    object = models.Manager()

    def __str__(self):
        return self.object_name
