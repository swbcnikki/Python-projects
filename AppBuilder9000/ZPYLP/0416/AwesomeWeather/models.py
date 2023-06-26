from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'cities'


Town = [
    ("Boaz", "Boaz"),
    ("Portland", "Portland"),
    ("Seattle", "Seattle"),
    ("Miami", "Miami"),
    ("Hilo", "Hilo"),
    ("El Paso", "El Paso"),
        ]

States = [
    ("AL", "AL"),
    ("OR", "OR"),
    ("WA", "WA"),
    ("FL", "FL"),
    ("HI", "HI"),
    ("TX", "TX"),

         ]


class Facts(models.Model):
    state = models.CharField(max_length=200, choices=States)
    town = models.CharField(max_length=200, choices=Town)
    date = models.DateField()
    event = models.TextField(max_length=2000)

    def __str__(self):
        return self.state
    objects = models.Manager()
    db_table = "Facts"



    


















