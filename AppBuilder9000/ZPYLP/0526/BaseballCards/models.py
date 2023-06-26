from django.db import models

position_choices = [
    ('P', 'P'),
    ('C', 'C'),
    ('1B', '1B'),
    ('2B', '2B'),
    ('3B', '3B'),
    ('SS', 'SS'),
    ('LF', 'LF'),
    ('CF', 'CF'),
    ('RF', 'RF'),
    ('DH', 'DH'),
]

bats_throws_choices = [
    ('R/R', 'R/R'),
    ('R/L', 'R/L'),
    ('L/L', 'L/L'),
    ('L/R', 'L/R'),
    ('S/R', 'S/R'),
    ('S/L', 'S/L'),
]

class BaseballCard(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    active = models.BooleanField(default=False)
    position = models.CharField(max_length=2, choices=position_choices)
    bats_throws = models.CharField(max_length=3, choices=bats_throws_choices)
    career_ba_or_era = models.DecimalField(max_digits=5, decimal_places=3)  # "batting average or earned run average"
    career_hr_or_so = models.IntegerField()   # "home runs or strikeouts"

    BaseballCards = models.Manager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name



