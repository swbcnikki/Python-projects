from django.db import models


# Create your models here.
# declare a new model with a name "ChefKnives
class ChefKnives(models.Model):
    # fields of the model
    brands = models.CharField(max_length=60)
    price = models.IntegerField(default='')
    country_origin = models.CharField(max_length=60)
    steal = models.CharField(max_length=60)
    blade_style = models.CharField(max_length=60)

    objects = models.Manager()

    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.brands
