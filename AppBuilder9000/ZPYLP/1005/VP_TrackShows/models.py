from django.db import models


Day_Of_Week = [
    ('Sunday', 'Sunday'),
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
]


Show_Status = [
    ('Continuing', 'Continuing'),
    ('Ended', 'Ended'),
]


class MyShows(models.Model):
    show_title = models.CharField(max_length=75, null=False)
    status = models.CharField(max_length=10, choices=Show_Status, null=True)
    day_of_week = models.CharField(max_length=20, choices=Day_Of_Week)
    airtime = models.TimeField(default='12:00')
    network = models.CharField(max_length=20)

    objects = models.Manager()

    def __str__(self):
        return self.show_title


class ShowInfo(models.Model):
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=500, default="", blank=True)
    year_first_aired = models.SmallIntegerField()
    number_of_seasons = models.SmallIntegerField()
    image = models.CharField(max_length=255, default="", blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.title
