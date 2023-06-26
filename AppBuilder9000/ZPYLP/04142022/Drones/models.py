from django.db import models


class Drone(models.Model):
    ROTORS = (
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('8', '8'),
    )
    BATTERY = (
        ('2s', '2s'),
        ('3s', '3s'),
        ('4s', '4s'),
        ('5s', '5s'),
        ('6s', '6s'),
    )
    drone_name = models.CharField(max_length=50)
    rotors = models.CharField(max_length=10,choices=ROTORS)
    battery = models.CharField(max_length=10, choices=BATTERY)
    prop_length= models.IntegerField(max_length=10)
    flight_time_in_minutes = models.IntegerField(max_length=10)




    Drones = models.Manager()

    def __str__(self):
        return self.drone_name