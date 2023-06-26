from django.db import models


class Review(models.Model):
    reviewer = models.CharField(max_length=100)
    game = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)
    review_score = models.DecimalField(max_digits=2, decimal_places=1)
    summary = models.TextField(max_length=500, default='')

    objects = models.Manager()

    def __str__(self):
        return self.game
