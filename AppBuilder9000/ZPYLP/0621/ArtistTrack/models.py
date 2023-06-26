from django.db import models


# Create your models here.
class Song(models.Model):
    GENRE_CHOICES = (
        ('rock', 'rock'),
        ('pop', 'pop'),
        ('classical', 'classical'),
        ('other', 'other'),
        ('nu-metal', 'nu-metal'),
        ('metalcore', 'metalcore'),
        ('death metal', 'death metal'),
        ('other', 'other'),
    )

    YEAR_CHOICES = [(r, r) for r in range(2022, 1950, -1)]

    song_name = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50, default=None, blank=True)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    year = models.IntegerField(choices=YEAR_CHOICES)
    lyrics = models.TextField(default=None, null=True)

    Songs = models.Manager()

    def __str__(self):
        return "{} by {}".format(self.song_name, self.artist)


class Playlist(models.Model):
    playlist_name = models.CharField(max_length=50)
    playlist_description = models.TextField()
    playlist_songs = models.ManyToManyField(Song)

    Playlists = models.Manager()

    def __str__(self):
        return self.playlist_name















