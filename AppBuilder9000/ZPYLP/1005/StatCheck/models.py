from django.db import models

class Player(models.Model):
    objects = models.Manager
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    what_position = models.CharField(max_length=30)
    what_number = models.IntegerField()
    strong_feet = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name


class Team(models.Model):
    team_name = models.ForeignKey(Player, on_delete=models.CASCADE)
    team_location = models.CharField(max_length=30)
    head_coach = models.CharField(max_length=30)
    team_mascot = models.CharField(max_length=30)
    team_record = models.IntegerField()

    objects = models.Manager()

    def __str__(self):
        return self.team_name