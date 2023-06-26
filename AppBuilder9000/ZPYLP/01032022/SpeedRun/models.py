from django.db import models
import datetime
from datetime import date


# game name model
class GameName(models.Model):
    game_name = models.CharField(max_length=60, default="")

    objects = models.Manager()

    def __str__(self):
        return self.game_name

# limiting choices of platforms
PLATFORM_CHOICES = (
    ('Atari 2600','Atari 2600'),
    ('Xbox','Xbox'),
    ('Xbox 360','Xbox 360'),
    ('Xbox One','Xbox One'),
    ('Xbox Series X','Xbox Series X'),
    ('NES','NES'),
    ('Game Boy','Game Boy'),
    ('SNES','SNES'),
    ('N64','N64'),
    ('Game Boy Advance','Game Boy Advance'),
    ('GameCube','GameCube'),
    ('Nintendo DS','Nintendo DS'),
    ('Wii','Wii'),
    ('Nintendo 3DS','Nintendo 3DS'),
    ('Wii U','Wii U'),
    ('Switch','Switch'),
    ('Sega Genesis','Sega Genesis'),
    ('PlayStation','PlayStation'),
    ('PlayStation 2','PlayStation 2'),
    ('PSP','PSP'),
    ('PlayStation 3','PlayStation 3'),
    ('PlayStation 4','PlayStation 4'),
    ('PlayStation 5','PlayStation 5'),
    ('PC','PC'),
)




# creating a speedrun class object
class Record(models.Model):
    player = models.CharField(max_length=60, default="")
    game = models.ForeignKey(GameName, related_name='records', on_delete=models.CASCADE)
    time = models.CharField(max_length=30, default="HH:MM:SS")
    platform = models.CharField(max_length=60, choices=PLATFORM_CHOICES, default="")
    date = models.DateField(default=date.today)

    objects = models.Manager()

    def __str__(self):
        return [self.player,
                self.time,
                self.platform,
                self.date]

