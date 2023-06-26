from django.db import models
from datetime import datetime, date

# Dropdown menu for genres
GENRE_CHOICES = [
    ('First Person Shooter', 'First Person Shooter'),
    ('Real Time Strategy', 'Real Time Strategy'),
    ('Role Playing Game', 'Role Playing Game'),
    ('Simulator', 'Simulator'),
    ('First Person Experience', 'First Person Experience'),
    ('Action/Adventure', 'Action/Adventure'),
    ('Massive Multiplayer Online', 'Massive Multiplayer Online'),
    ('Racing', 'Racing'),
    ('Sports', 'Sports'),
    ('Virtual Reality', 'Virtual Reality'),
    ('Indie Game', 'Indie Game'),
    ('Builder/Survival', 'Builder/Survival'),
    ('Open World', 'Open World'),
    ('Turn Based Tactics', 'Turn Based Tactics'),
]
# Dropdown menu for Online game store
STORE_CHOICES = [
    ('Steam', 'Steam'),
    ('Epic Games', 'Epic Games'),
    ('Good Old Games', 'Good Old Games'),
    ('Battle.net', 'Battle.net'),
    ('Origin', 'Origin'),
    ('Oculus', 'Oculus'),
    ('Uplay', 'Uplay'),
]
# Database model for games owned
class Games(models.Model):
    game_name = models.CharField(max_length=50, default="", blank=False)
    genre = models.CharField(max_length=50, default="", choices=GENRE_CHOICES)
    store_name = models.CharField(max_length=50, default="", choices=STORE_CHOICES)
    game_key = models.CharField(max_length=75, default="", blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.game_name

# Database model for owned DLC that belongs to games owned
class Dlc(models.Model):
    base_game = models.CharField(max_length=50, default="", blank=False) #To be referenced as a foreign key that links to Games.game_name
    dlc_name = models.CharField(max_length=50, default="", blank=False)
    dlc_key = models.CharField(max_length=75, default="", blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.base_game + ' ' + self.dlc_name

class Wishlist(models.Model):
    game_title = models.CharField(max_length=50, default="", blank=False)
    genre = models.CharField(max_length=50, default="", choices=GENRE_CHOICES)
    store_name = models.CharField(max_length=50, default="", choices=STORE_CHOICES)
    release_date = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.game_title

