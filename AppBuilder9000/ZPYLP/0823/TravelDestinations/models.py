from django.db import models


# choices for state
StateChoices = [
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
    ('Virginia', 'Virginia'),
    ('Washington', 'Washington'),
    ('West Virginia', 'West Virginia'),
    ('Wisconsin', 'Wisconsin'),
    ('Wyoming', 'Wyoming'),
]


# created a class and defined its attributes


class destination(models.Model):
    TripName = models.CharField(max_length=30, default="", blank=False, null=False)
    City = models.CharField(max_length=20, default="", blank=False, null=False)
    State = models.CharField(max_length=20, choices=StateChoices, blank=True)
    Country = models.CharField(max_length=20, default="", blank=True, null=False)
    Notes = models.TextField(max_length=300, default="Notes", blank=True)

    # assigns a manager
    destination = models.Manager()
