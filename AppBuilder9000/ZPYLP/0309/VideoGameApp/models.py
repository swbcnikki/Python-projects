from django.db import models

# Create your models here.
GENRE_CHOICES = [
    ('Role-Playing Game', 'Role-Playing Game'),
    ('First-Person Shooter', 'First-Person Shooter'),
    ('Third-Person Shooter', 'Third-Person shooter'),
    ('2D Platform', '2D Platform'),
    ('3D Platform', '3D Platform'),
    ('Metroidvania', 'Metroidvania'),
    ('Puzzle', 'Puzzle'),
    ('Simulation', 'Simulation'),
]

PLATFORM_CHOICES = [
    ('Android', 'Android'),
    ('iOS', 'iOS'),
    ('Nintendo Entertainment System', 'Nintendo Entertainment System'),
    ('Super Nintendo Entertainment System', 'Super Nintendo Entertainment System'),
    ('Sega Genesis', 'Sega Genesis'),
    ('Sega Dreamcast', 'Sega Dreamcast'),
    ('Sony Playstation', 'Sony Playstation'),
    ('Sony Playstation 2', 'Sony Playstation 2'),
    ('Sony Playstation 3', 'Sony Playstation 3'),
    ('Sony Playstation 4', 'Sony Playstation 4'),
    ('Microsoft XBox', 'Microsoft XBox'),
    ('Microsoft XBox 360', 'Microsoft XBox 360'),
    ('Microsoft XBox One', 'Microsoft XBox One'),
]


class VideoGames(models.Model):
    Title = models.CharField(max_length=100)
    Platform = models.CharField(max_length=100, choices=PLATFORM_CHOICES)
    Genre = models.CharField(max_length=100, choices=GENRE_CHOICES)
    Opinion = models.TextField(max_length=500)

    objects = models.Manager()

    def __str__(self):
        return self.Title


