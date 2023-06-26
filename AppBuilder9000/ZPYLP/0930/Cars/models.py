from django.db import models

class description(models.Model):
    make = models.CharField(max_length=60, default='', null=False)
    model = models.CharField(max_length=60, default='', null=False)
    first_name = models.CharField(max_length=60, default='', null=False)
    last_name = models.CharField(max_length=60, default='', null=False)
    description = models.TextField(max_length=300, default='', null=False)

    objects = models.Manager()

    def __str__(self):
        return self.model

