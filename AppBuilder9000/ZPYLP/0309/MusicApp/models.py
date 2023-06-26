from django.db import models
import datetime


# Create your models here.
GROUP_OR_SOLO_CHOICES = [
    ('group', 'group'),
    ('solo', 'solo'),
]


class MusicalArtists(models.Model):
    artist_name = models.CharField(max_length=60, default="", blank=True, null=False)
    group_or_solo = models.CharField(max_length=5, choices=GROUP_OR_SOLO_CHOICES)
    genre = models.CharField(max_length=20, default="", blank=True, null=False)
    year_formed = models.PositiveIntegerField(default=1900,  blank=True, null=False)
    active = models.BooleanField(blank=False, null=False)
    image_url = models.CharField(max_length=250, default="", blank=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.artist_name


class AlbumNames(models.Model):
    album_name = models.CharField(max_length=100, default="", blank=True, null=False)
    artist_name = models.CharField(max_length=60, default="", blank=True, null=False)
    date_album_released = models.DateField(("Date Album Released"), default=datetime.date.today)
    number_of_tracks = models.PositiveIntegerField(default=1, blank=True, null=False)
    genre = models.CharField(max_length=20, default="", blank=True, null=False)
    img_url = models.CharField(max_length=250, default="", blank=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.album_name



class SongNames(models.Model):
    song_name = models.CharField(max_length=100, default="", blank=True, null=False)
    artist_name = models.CharField(max_length=60, default="", blank=True, null=False)
    album_name = models.CharField(max_length=100, default="", blank=True, null=False)
    song_length = models.CharField(max_length=50, default="", blank=True, null=False)
    song_release_year = models.PositiveIntegerField(default=1990, blank=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.song_name




