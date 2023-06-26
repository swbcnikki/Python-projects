from django.db import models

LOCATION_CHOICES = [
    ('Alabama', 'Alabama'),
    ('Alaska', 'Alaska'),
    ('Arizona', 'Arizona'),
    ('Arkansas', 'Arkansas'),
    ('California', 'California'),
    ('Colorado', 'Colorado'),
    ('Connecticut', 'Connecticut'),
    ('Delaware', 'Delaware'),
    ('Florida', 'Florida'),
    ('Georgia', 'Georgia'),
    ('Hawaii', 'Hawaii'),
    ('Idaho', 'Idaho'),
    ('Illinois', 'Illinois'),
    ('Indiana', 'Indiana'),
    ('Iowa', 'Iowa'),
    ('Kansas', 'Kansas'),
    ('Kentucky', 'Kentucky'),
    ('Louisiana', 'Louisiana'),
    ('Maine', 'Maine'),
    ('Maryland', 'Maryland'),
    ('Massachusetts', 'Massachusetts'),
    ('Michigan', 'Michigan'),
    ('Minnesota', 'Minnesota'),
    ('Mississippi', 'Mississippi'),
    ('Missouri', 'Missouri'),
    ('Montana', 'Montana'),
    ('Nebraska', 'Nebraska'),
    ('Nevada', 'Nevada'),
    ('New Hampshire', 'New Hampshire'),
    ('New Jersey', 'New Jersey'),
    ('New Mexico', 'New Mexico'),
    ('New York', 'New York'),
    ('North Carolina', 'North Carolina'),
    ('North Dakota', 'North Dakota'),
    ('Ohio', 'Ohio'),
    ('Oklahoma', 'Oklahoma'),
    ('Oregon', 'Oregon'),
    ('Pennsylvania', 'Pennsylvania'),
    ('Rhode Island', 'Rhode Island'),
    ('South Carolina', 'South Carolina'),
    ('South Dakota', 'South Dakota'),
    ('Tennessee', 'Tennessee'),
    ('Texas', 'Texas'),
    ('Utah', 'Utah'),
    ('Vermont', 'Vermont'),
    ('Virgina', 'Virgina'),
    ('Washington', 'Washington'),
    ('West Virginia', 'West Virginia'),
    ('Wisconsin', 'Wisconsin'),
    ('Wyoming', 'Wyoming'),
]

DIFFICULTY_CHOICES = [
    ('Easy','Easy'),
    ('Medium','Medium'),
    ('Hard','Hard'),
]

class Trails(models.Model):
    name = models.CharField(max_length=100, default="", blank=False, null=False)  #name is required
    location = models.CharField(max_length=60, choices=LOCATION_CHOICES)
    difficulty = models.CharField(max_length=60, choices=DIFFICULTY_CHOICES, default='')
    miles = models.DecimalField(default=0.0, max_digits=10000, decimal_places=1)
    camping = models.NullBooleanField()
    description = models.TextField(max_length=300, default="", blank=True)
    image = models.CharField(max_length=300, default="", blank=True, null=False)
    objects = models.Manager()

    def __str__(self):
        return self.name

    #look into adding map coordinates for API


#work on creating relational tables