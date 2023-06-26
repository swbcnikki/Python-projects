from django.db import models

mounth_choices = [
    ('January', 'January'),
    ('February', 'February'),
    ('March', 'March'),
    ('April', 'April'),
    ('May', 'May'),
    ('June', 'June'),
    ('July', 'July'),
    ('August', 'August'),
    ('September', 'September'),
    ('October', 'October'),
    ('November', 'November'),
    ('December', 'December'),
]

day_choices = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
    ('13', '13'),
    ('14', '14'),
    ('15', '15'),
    ('16', '16'),
    ('17', '17'),
    ('18', '18'),
    ('19', '19'),
    ('20', '20'),
    ('21', '21'),
    ('22', '22'),
    ('23', '23'),
    ('24', '24'),
    ('25', '25'),
    ('26', '26'),
    ('27', '27'),
    ('28', '28'),
    ('29', '29'),
    ('30', '30'),
    ('31', '31'),
]

vehicle_type = [
    ('SUV', 'SUV'),
    ('Truck', 'Truck'),
    ('Trailer', 'Trailer'),
    ('Big Truck', 'Big Truck'),
    ('Move Box', 'Move Box'),
]

class Movestate(models.Model):
    State = models.CharField(max_length=50)
    Sity = models.CharField(max_length=60)
    Month = models.CharField(max_length=60, choices=mounth_choices)
    Day = models.CharField(max_length=60, default="", choices=day_choices)
    description = models.TextField(max_length=500, default="", blank=True)
    Movers = models.Manager()

class VehicleType(Movestate):
    Vehicle_Type = models.CharField(max_length=60, choices=vehicle_type)
    Movers = models.CharField(max_length=50)


    objects = models.Manager()

    def __str__(self):
        return self.state
