from django.db import models

# Create your models here.

# state choices and beer specialty choices
BEER_CHOICES = [('IPAS', 'IPAs'),
                ('SOURS', 'Sours'),
                ('BARREL-AGED', 'Barrel-Aged'),
                ('DESSERT', 'Dessert/Fruited')
                ]


STATE_CHOICES = [
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

# brewery models, only second beerstyle and notes can be empty
class Brewery(models.Model):
    name = models.CharField(max_length=50, default='', blank=False, null=False)
    address1 = models.CharField(max_length=50, default='', blank=False, null=False)
    address2 = models.CharField(max_length=50, default='', blank=True, null=True)
    city = models.CharField(max_length=50, default='', blank=False, null=False)
    state = models.CharField(max_length=50, default='Select State', choices=STATE_CHOICES, blank=False, null=False)
    zip = models.IntegerField(blank=False, null=False)
    beerstyles1 = models.CharField(max_length=50, default='', choices=BEER_CHOICES, blank=False, null=False)
    beerstyles2 = models.CharField(max_length=50, default='', choices=BEER_CHOICES, blank=True, null=True)
    notes = models.TextField(max_length=250, default='', blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return self.name


class AllBreweries(models.Model):
    allbreweries = Brewery.objects.all()
