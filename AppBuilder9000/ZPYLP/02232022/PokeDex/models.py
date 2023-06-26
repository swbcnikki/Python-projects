from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=100, default="")
    type = models.CharField(max_length=50, default="", blank=True)
    abilities = models.CharField(max_length=100, default="", blank=True)

    object = models.Manager()

    def __str__(self):
        return self.name