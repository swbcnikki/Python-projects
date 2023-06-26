from django.db import models

class Traveler(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 254)


    travelers = models.Manager()



    def __str__(self):
        return self.first_name + ' ' + self.last_name




class Place(models.Model):
    place = models.CharField(max_length = 100)
    description= models.TextField(max_length=500, default='', blank=True, null=False)
    price = models.DecimalField(default=0.00, max_digits=10000, decimal_places = 2)


    places = models.Manager()

    def __str__(self):
        return self.place




