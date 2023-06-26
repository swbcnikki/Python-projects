from django.db import models

# Create your models here.


class Piece(models.Model):
    piece_name = models.CharField(max_length=50)
    piece_composer = models.CharField(max_length=25)

    pieces = models.Manager()

    def __str__(self):
        return self.piece_name + ' ' + self.piece_composer


class Conductor(models.Model):
    conductor_name = models.CharField(max_length=25)

    conductors = models.Manager()

    def __str__(self):
        return self.conductor_name


class Orchestra(models.Model):
    orchestra_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    artistic_director = models.ForeignKey(Conductor, on_delete=models.CASCADE,)

    orchestras = models.Manager()

    def __str__(self):
        return self.orchestra_name


class Concert(models.Model):
    event_name = models.CharField(max_length=100)
    orchestra = models.ForeignKey(Orchestra, on_delete=models.CASCADE,)
    pieces = models.ManyToManyField(Piece)
    conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE,)
    date = models.DateField()

    concerts = models.Manager()

    def __str__(self):
        return self.event_name
