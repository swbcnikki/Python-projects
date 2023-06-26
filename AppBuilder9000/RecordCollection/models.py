from django.db import models

MEDIA_TYPE = (
    ('VI', 'Vinyl'),
    ('CD', 'CD'),
    ('CA', 'Cassette'),
    ('OT', 'Other')
)

QUALITY_TYPE = (
    ('MT', 'Mint'),
    ('NM', 'Near Mint'),
    ('EX', 'Excellent'),
    ('VG', 'Very Good'),
    ('GD', 'Good'),
    ('PR', 'Poor'),
    ('MT', 'Mint'),
)

RATING_TYPE = (
    (5, '5 Stars'),
    (4, '4 Stars'),
    (3, '3 Stars'),
    (2, '2 Stars'),
    (1, '1 Star'),
)


class Records(models.Model):
    artistFN = models.CharField("Artist (Band or First Name)", max_length=100, default="")
    artistLN = models.CharField("Artist Last Name (if applicable)", max_length=100, default="", blank=True)
    title = models.CharField("Album Title", max_length=100, default="")
    format = models.CharField("Format", max_length=2, choices=MEDIA_TYPE)
    quality = models.CharField("Condition", max_length=2, choices=QUALITY_TYPE, blank=True)
    rating = models.IntegerField("Personal Rating", choices=RATING_TYPE, blank=True)
    comments = models.TextField("Notes", max_length=256, default="", blank=True)

    Records = models.Manager()

    def __str__(self):
        return self.title
