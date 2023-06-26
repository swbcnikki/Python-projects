from django.db import models


Rating_Choices = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
)


class Review(models.Model):
    AnimeName = models.CharField(max_length=100)
    Genre = models.CharField(max_length=100)
    About = models.TextField(max_length=500, default="about")
    Rating = models.CharField(max_length=20)
    Review = models.TextField(max_length=500)

    def __str__(self):
        return self.AnimeName + ': Rated ' + self.Rating

    objects = models.Manager()






