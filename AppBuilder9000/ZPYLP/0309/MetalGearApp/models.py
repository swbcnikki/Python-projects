from django.db import models

# Create your models here.
SPECIALIZATION_CHOICES = [
    ('Research And Development', 'Research and Development'),
    ('Intel', 'Intel'),
    ('Command', 'Command'),
    ('Combat', 'Combat'),
    ('Medical', 'Medical'),
    ('Base Development', 'Base Development'),
    ('Support', 'Support'),
    ('Animal Conservation', 'Animal Conservation'),
]

CODE_PREFIX_CHOICES = [
    ('Solid', 'Solid'),
    ('Liquid', 'Liquid'),
    ('Solidus', 'Solidus'),
    ('Charging', 'Charging'),
    ('Psycho', 'Psycho'),
    ('Arsenal', 'Arsenal'),
    ('Revolver', 'Revolver'),
    ('Killer', 'Killer'),
    ('White', 'White'),
    ('Black', 'Black'),
    ('Screaming', 'Screaming'),
    ('Raging', 'Raging'),
    ('Crying', 'Crying'),
    ('Decoy', 'Decoy'),
    ('Sniper', 'Sniper'),
]

CODE_SUFFIX_CHOICES = [
    ('Wolf', 'Wolf'),
    ('Snake', 'Snake'),
    ('Mantis', 'Mantis'),
    ('Raven', 'Raven'),
    ('Rhino', 'Rhino'),
    ('Ocelot', 'Ocelot'),
    ('Tiger', 'Tiger'),
    ('Shark', 'Shark'),
    ('Fox', 'Fox'),
    ('Panther', 'Panther'),
    ('Eagle', 'Eagle'),
    ('Jackal', 'Jackal'),
    ('Zebra', 'Zebra'),
    ('Deer', 'Deer'),
    ('Elephant', 'Elephant'),
    ('Hippopotamus', 'Hippopotamus'),
    ('Turtle', 'Turtle'),
    ('Chicken', 'Chicken'),
]

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
    ('Prefer not to say ', 'Prefer not to say'),
]


class DiamondDogList(models.Model):
    fName = models.CharField(max_length=20, blank=False, null=False)
    lName = models.CharField(max_length=20, blank=False, null=False)
    gender = models.CharField(max_length=30, blank=False, choices=GENDER_CHOICES)
    specialization = models.CharField(max_length=50, blank=False,  choices=SPECIALIZATION_CHOICES)
    codePrefix = models.CharField(max_length=30, blank=False, choices=CODE_PREFIX_CHOICES)
    codeSuffix = models.CharField(max_length=50, blank=False, choices=CODE_SUFFIX_CHOICES)
    email = models.EmailField(max_length=100, default="", blank=True)

    objects = models.Manager()

    def __str__(self):
        return "{}-{}".format(self.fName, self.lName)
