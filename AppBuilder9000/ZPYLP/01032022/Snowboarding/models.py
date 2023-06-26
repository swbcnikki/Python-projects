from django.db import models

class Ryder(models.Model):
    First_Name = models.CharField(max_length=60, default="", blank=True, null=False)
    Last_Name = models.CharField(max_length=60, default="", blank=True, null=False)
    Style = models.CharField(max_length=60, default="", blank=True, null=False)
    Sponsor = models.CharField(max_length=60, default="", blank=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.First_Name + ' ' + self.Last_Name

