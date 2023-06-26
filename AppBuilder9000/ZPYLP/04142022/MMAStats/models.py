from django.db import models

# creating initial model, this
# holds our details for the fighters.

class Champions(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    defenses = models.IntegerField(default=0)
    p4p_rank = models.IntegerField(default=0)
    record = models.CharField(max_length=20)

    objects = models.Manager()

    def __str__(self):
        return self.first_name
