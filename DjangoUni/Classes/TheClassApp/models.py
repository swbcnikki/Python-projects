from django.db import models

# Create your models here.
UNIT_CHOICES = [
    ('adulting', 'adulting'),
    ('peopling', 'peopling'),
    ('crisis', 'crisis'),
]


class djangoClasses(models.Model):
    title = models.CharField(max_length=30, choices=UNIT_CHOICES)
    CourseNum = models.IntegerField(default=000, blank=True, null=False)
    Instr = models.CharField(max_length=30, default='', blank=True, null=False)
    Duration = models.DecimalField(default=00.00, max_digits=5, decimal_places=2)


    objects = models.Manager()

    def __str__(self):
        return self.title