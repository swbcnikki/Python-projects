from django.db import models


class Youtuber(models.Model):
    YTname = models.CharField(max_length=100)
    YTlink = models.CharField(max_length=100)
    # YTlink above /\ will change from a empty field to the info I scrape with beautiful soup.

    # using the models manager to return the name of the Youtuber
    objects = models.Manager()

    def __str__(self):
        return self.YTname