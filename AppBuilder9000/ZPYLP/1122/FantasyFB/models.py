from django.db import models

# Create your models here.


class Player(models.Model):
    POSITION_CHOICES = [
        ('QB', 'Quarterback'),
        ('RB', 'Running Back'),
        ('FB', 'Full Back'),
        ('WR', 'Wide Receiver'),
        ('TE', 'Tight End'),
        ('DL', 'Defensive Lineman'),
        ('LB', 'Linebacker'),
        ('S', 'Safety'),
        ('CB', 'Cornerback'),
        ('K', 'Kicker'),
        ('C', 'Coach'),
    ]

    TEAM_CHOICES = [
        ('Marvel', 'Marvel'),
        ('DC', 'DC'),
    ]

    name = models.CharField(max_length=50, default="", null=False)
    team = models.CharField(max_length=6, choices=TEAM_CHOICES)
    position = models.CharField(max_length=2, choices=POSITION_CHOICES)
    reason = models.TextField(max_length=500, default="", null=False)

    Players = models.Manager()

    def __str__(self):
        return self.name
