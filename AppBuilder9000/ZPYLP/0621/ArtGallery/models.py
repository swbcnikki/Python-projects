from django.db import models

class Artist(models.Model):
    First_Name = models.CharField(max_length=40)
    Last_Name = models.CharField(max_length=40)
    Email = models.CharField(max_length=60, help_text='Please make sure your email is correct!')
    ART_TYPE = (
        ('T', 'Traditional'),
        ('O', 'Oil'),
        ('W', 'Watercolor'),
        ('D', 'Digital'),
        ('A', 'Acrylic'),
        ('P', 'Pottery'),
        ('S', 'Sculpture'),
    )
    Art_Type = models.CharField(max_length=1, choices=ART_TYPE)
    Picture = models.URLField(max_length=200)

    Artists = models.Manager()

    def __str__(self):
        return self.First_Name


