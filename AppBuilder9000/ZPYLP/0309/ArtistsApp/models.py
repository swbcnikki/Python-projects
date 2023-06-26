from django.db import models

class Art(models.Model):
    piece_title = models.CharField(max_length=60 , null=False)
    artist = models.CharField(max_length=60, null=False)
    created_date = models.CharField(max_length=60, null=False)
    type = models.CharField(max_length=60 , null=False)

    object = models.Manager()

    def __str__(self):
        return self.piece_title