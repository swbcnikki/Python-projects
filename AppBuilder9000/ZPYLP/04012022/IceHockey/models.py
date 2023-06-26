from django.db import models


# Create your models here.


class Profile(models.Model):
    TEAM_OPTIONS = (
        ('Anaheim Ducks', 'Anaheim Ducks'),
        ('Arizona Coyotes', 'Arizona Coyotes'),
        ('Boston Bruins', 'Boston Bruins'),
        ('Buffalo Sabres', 'Buffalo Sabres'),
        ('Calgary Flames', 'Calgary Flames'),
        ('Carolina Hurricanes', 'Carolina Hurricanes'),
        ('Colorado Avalanche', 'Colorado Avalanche'),
        ('Columbus Blue Jackets', 'Columbus Blue Jackets'),
        ('Dallas Stars', 'Dallas Stars'),
        ('Detroit Red Wings', 'Detroit Red Wings'),
        ('Edmonton Oilers', 'Edmonton Oilers'),
        ('Florida Panthers', 'Florida Panthers'),
        ('Los Angeles Kings', 'Los Angeles Kings'),
        ('Minnesota Wild', 'Minnesota Wild'),
        ('Montreal Canadiens', 'Montreal Canadiens'),
        ('Nashville Predators', 'Nashville Predators'),
        ('New Jersey Devils', 'New Jersey Devils'),
        ('New York Rangers', 'New York Rangers'),
        ('New York Islanders', 'New York Islanders'),
        ('Ottawa Senators', 'Ottawa Senators'),
        ('Philadelphia Flyers', 'Philadelphia Flyers'),
        ('Pittsburgh Penguins', 'Pittsburgh Penguins'),
        ('San Jose Sharks', 'San Jose Sharks'),
        ('Seattle Kraken', 'Seattle Kraken'),
        ('St. Louis Blues', 'St. Louis Blues'),
        ('Tampa Bay Lightning', 'Tampa Bay Lightning'),
        ('Toronto Maple Leafs', 'Toronto Maple Leafs'),
        ('Vancouver Canucks', 'Vancouver Canucks'),
        ('Vegas Golden Knights', 'Vegas Golden Knights'),
        ('Washington Capitals', 'Washington Capitals'),
        ('Winnipeg Jets', 'Winnipeg Jets'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    favorite_team = models.CharField(max_length=30, choices=TEAM_OPTIONS)
    favorite_player = models.CharField(max_length=50)
    favorite_player_list = models.ManyToManyField(
        'FavPlayer', related_name='favorite', default=None, blank=True
    )

    Profile = models.Manager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class FavPlayer(models.Model):
    my_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='')
    number = models.PositiveSmallIntegerField(default=1)
    position = models.CharField(max_length=2)

    FavPlayer = models.Manager()

    class Meta:
        unique_together = ('my_profile', 'name')

    def __str__(self):
        return self.name
