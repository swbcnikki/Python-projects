from django.db import models

# Create your models here.
class Archive(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=60, default="", blank=True, null=False)
    author = models.CharField(max_length=60, default="", blank=True)
    number_of_pages_read = models.IntegerField()
    description_of_passage_read = models.TextField(max_length=300, default="", blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.title
