from django.db import models


# Create your models here.

NBA_TEAM = [
    ('Atlanta Hawks', 'Atlanta Hawks'),
    ('Boston Celtics', 'Boston Celtics'),
    ('Brooklyn Nets', 'Brooklyn Nets'),
    ('Charlotte Hornets', 'Charlotte Hornets'),
    ('Chicago Bulls', 'Chicago Bulls'),
    ('Cleveland Cavaliers', 'Cleveland Cavaliers'),
    ('Dallas Mavericks', 'Dallas Mavericks'),
    ('Denver Nuggets', 'Denver Nuggets'),
    ('Detroit Pistons', 'Detroit Pistons'),
    ('Golden State Warriors', 'Golden State Warriors'),
    ('Houston Rockets', 'Houston Rockets'),
    ('Indiana Pacers', 'Indiana Pacers'),
    ('Los Angeles Clippers', 'Los Angeles Clippers'),
    ('Los Angeles Lakers', 'Los Angeles Lakers'),
    ('Memphis Grizzlies', 'Memphis Grizzlies'),
    ('Miami Heat', 'Miami Heat'),
    ('Milwaukee Bucks', 'Milwaukee Bucks'),
    ('Minnesota Timberwolves', 'Minnesota Timberwolves'),
    ('New Orleans Pelicans', 'New Orleans Pelicans'),
    ('New York Knicks', 'New York Knicks'),
    ('Oklahoma City Thunder', 'Oklahoma City Thunder'),
    ('Orlando Magic', 'Orlando Magic'),
    ('Philadelphia 76ers', 'Philadelphia 76ers'),
    ('Phoenix Suns', 'Phoenix Suns'),
    ('Portland Trailblazers', 'Portland Trailblazers'),
    ('Sacramento Kings', 'Sacramento Kings'),
    ('San Antonio Spurs', 'San Antonio Spurs'),
    ('Toronto Raptors', 'Toronto Raptors'),
    ('Utah Jazz', 'Utah Jazz'),
    ('Washington Wizards', 'Washington Wizards'),
]

AWAY_TEAM = [
    ('Atlanta Hawks', 'Atlanta Hawks'),
    ('Boston Celtics', 'Boston Celtics'),
    ('Brooklyn Nets', 'Brooklyn Nets'),
    ('Charlotte Hornets', 'Charlotte Hornets'),
    ('Chicago Bulls', 'Chicago Bulls'),
    ('Cleveland Cavaliers', 'Cleveland Cavaliers'),
    ('Dallas Mavericks', 'Dallas Mavericks'),
    ('Denver Nuggets', 'Denver Nuggets'),
    ('Detroit Pistons', 'Detroit Pistons'),
    ('Golden State Warriors', 'Golden State Warriors'),
    ('Houston Rockets', 'Houston Rockets'),
    ('Indiana Pacers', 'Indiana Pacers'),
    ('Los Angeles Clippers', 'Los Angeles Clippers'),
    ('Los Angeles Lakers', 'Los Angeles Lakers'),
    ('Memphis Grizzlies', 'Memphis Grizzlies'),
    ('Miami Heat', 'Miami Heat'),
    ('Milwaukee Bucks', 'Milwaukee Bucks'),
    ('Minnesota Timberwolves', 'Minnesota Timberwolves'),
    ('New Orleans Pelicans', 'New Orleans Pelicans'),
    ('New York Knicks', 'New York Knicks'),
    ('Oklahoma City Thunder', 'Oklahoma City Thunder'),
    ('Orlando Magic', 'Orlando Magic'),
    ('Philadelphia 76ers', 'Philadelphia 76ers'),
    ('Phoenix Suns', 'Phoenix Suns'),
    ('Portland Trailblazers', 'Portland Trailblazers'),
    ('Sacramento Kings', 'Sacramento Kings'),
    ('San Antonio Spurs', 'San Antonio Spurs'),
    ('Toronto Raptors', 'Toronto Raptors'),
    ('Utah Jazz', 'Utah Jazz'),
    ('Washington Wizards', 'Washington Wizards'),

]


class SavedNbaGame(models.Model):
    email = models.EmailField(max_length=50, blank=False, null=False)
    home_team = models.CharField(max_length=50, blank=False, choices=NBA_TEAM)
    away_team = models.CharField(max_length=50, blank=False, choices=NBA_TEAM)
    date_game = models.DateField(blank=False)
    time_start = models.TimeField(blank=False)
    game_notes = models.TextField(max_length=250, default="", blank=True, null=True)

    SavedNbaGame = models.Manager()

    def __str__(self):
        return "{} vs {} on {} at {}".format(self.home_team, self.away_team, self.date_game, self.time_start)


class FavPlayer(models.Model):
    email = models.EmailField(max_length=50, blank=False, null=False)
    fav_player = models.CharField(max_length=50, blank=False)
    corresponding_team = models.CharField(max_length=50, blank=False, choices=NBA_TEAM)

    FavPlayer = models.Manager()

    def __str__(self):
        return "Hello {}, {} is playing tonight! Tune in and watch!".format(self.email, self.fav_player)
