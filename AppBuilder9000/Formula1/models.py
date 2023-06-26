from django.db import models

##ADDING IN ALL DATA NEEDED FOR RESULTS FORM DROPDOWNS
DRIVER_CHOICES = [
    ('', 'Select a Driver'),
    ('Alex Albon', 'Alex Albon'),
    ('Fernando Alonso', 'Fernando Alonso'),
    ('Valterri Bottas', 'Valterri Bottas'),
    ('Pierre Gasly', 'Pierre Gasly'),
    ('Lewis Hamilton', 'Lewis Hamilton'),
    ('Nicholas Latifi', 'Nicholas Latifi'),
    ('Charles Leclerc', 'Charles Leclerc'),
    ('Kevin Magnussen', 'Kevin Magnussen'),
    ('Lando Norris', 'Lando Norris'),
    ('Esteban Ocon', 'Esteban Ocon'),
    ('Sergio Perez', 'Sergio Perez'),
    ('Daniel Ricciardo', 'Daniel Ricciardo'),
    ('George Russell', 'George Russell'),
    ('Carlos Sainz', 'Carlos Sainz'),
    ('Mick Schumacher', 'Mick Schumacher'),
    ('Lance Stroll', 'Lance Stroll'),
    ('Yuki Tsunoda', 'Yuki Tsunoda'),
    ('Max Verstappen', 'Max Verstappen'),
    ('Sebastian Vettel', 'Sebastian Vettel'),
    ('Zhou Guanyu', 'Zhou Guanyu'),
]

TEAM_CHOICES = [
    ('', 'Select a Team'),
    ('Alfa Romeo', 'Alfa Romeo'),
    ('Alpha Tauri', 'Alpha Tauri'),
    ('Alpine', 'Alpine'),
    ('Aston Martin', 'Aston Martin'),
    ('Ferrari', 'Ferrari'),
    ('Haas', 'Haas'),
    ('McLaren', 'McLaren'),
    ('Mercedes', 'Mercedes'),
    ('Red Bull', 'Red Bull'),
    ('Williams', 'Williams'),
]

RACE_CHOICES = [
    ('', 'Select a Race'),
    ('Bahrain', 'Bahrain'),
    ('Saudi Arabia', 'Saudi Arabia'),
    ('Australia', 'Australia'),
    ('Imola', 'Imola'),
    ('Miami', 'Miami'),
    ('Barcelona', 'Barcelona'),
    ('Monaco', 'Monaco'),
    ('Azerbaijan', 'Azerbaijan'),
    ('Canada', 'Canada'),
    ('Silverstone', 'Silverstone'),
    ('Austria', 'Austria'),
    ('France', 'France'),
    ('Hungary', 'Hungary'),
    ('Spa-Francorchamps', 'Spa-Francorchamps'),
    ('Zandvoort', 'Zandvoort'),
    ('Monza', 'Monza'),
    ('Singapore', 'Singapore'),
    ('Japan', 'Japan'),
    ('COTA', 'COTA'),
    ('Mexico', 'Mexico'),
    ('Brazil', 'Brazil'),
    ('Abu Dhabi', 'Abu Dhabi'),
]

FINISH_POSITION_CHOICES = [
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
    ('DNF', 'DNF'),
]

RACE_TYPE_CHOICES = [
    ('Sprint Race', 'Sprint Race'),
    ('Feature Race', 'Feature Race'),
]

## RESULTS MODEL SETUP
class Result(models.Model):
    Driver_Race_Key = models.CharField(max_length=100, default="", blank=False, null=False, unique=True)
    Driver_Name = models.CharField(max_length=30, default="", blank=False, null=False, choices=DRIVER_CHOICES)
    Current_Team = models.CharField(max_length=30, default="", blank=False, null=False, choices=TEAM_CHOICES)
    Race = models.CharField(max_length=50, default="", blank=False, null=False, choices=RACE_CHOICES)
    Race_Type = models.CharField(max_length=15, default="Feature Race", blank=False, null=False, choices=RACE_TYPE_CHOICES)
    Finishing_Position = models.CharField(max_length=5, default="", choices=FINISH_POSITION_CHOICES, blank=False, null=False)
    Fastest_Lap = models.BooleanField()
    Points_Earned = models.DecimalField(max_digits=2, decimal_places=0, default="", blank=False, null=False)

    results = models.Manager()

    def __str__(self):
        return f"{self.Race} - {self.Driver_Name} finished in position {self.Finishing_Position} and scored {self.Points_Earned} points."