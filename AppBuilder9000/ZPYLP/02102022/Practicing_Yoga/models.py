from django.db import models

# Choices for yoga type selector
TYPE_CHOICES = (
    ('Hatha', 'Hatha'),
    ('Iyengar', 'Iyengar'),
    ('Vinyasa ', 'Vinyasa '),
    ('Hot yoga', 'Hot yoga'),
    ('Ashtanga', 'Ashtanga'),
)


# Main model of yoga in detail
class Yoga(models.Model):
    type = models.CharField(choices=TYPE_CHOICES, max_length=30)
    name = models.CharField(max_length=30)
    benefits = models.CharField(max_length=200)

    objects = models.Manager()


def __str__(self):
    return self.type

