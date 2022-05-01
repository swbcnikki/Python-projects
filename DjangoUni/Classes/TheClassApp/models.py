from django.db import models

# Create your models here.
UNIT_CHOICES = {
    ('adulting', 'adulting'),
    ('peopling', 'peopling'),
    ('crisis', 'crisis'),
}
#creating the objects and their attributes
class djangoClasses(models.Model):
    title = models.CharField(max_length=30, choices=UNIT_CHOICES)
    CourseNum = models.IntegerField(default=000)
    Instr = models.CharField(max_length=30, default='', blank=True, null=False)
    Duration = models.DecimalField(default=00.00, max_digits=5, decimal_places=2)

class prereq(models.Model): #required prereq for each class
    title = models.CharField(max_length=30, choices=UNIT_CHOICES)
    CourseNum = models.IntegerField(default=000)

class book(models.Model): #the subject will determine the book
    title = models.CharField(max_length=30, choices=UNIT_CHOICES)

    objects = models.Manager()

    def __str__(self):
        return self.title