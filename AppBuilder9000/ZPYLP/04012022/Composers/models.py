from django.db import models

EraTypes = [('Classical', 'Classical'), ('Romantic', 'Romantic'), ('Baroque', 'Baroque'), ('20th Century', '20th Century')]


# Create your models here.
class Composer(models.Model):
    type = models.CharField(max_length=15,choices=EraTypes)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_year = models.DecimalField(max_digits=4,decimal_places=0)
    death_year = models.DecimalField(max_digits=4,decimal_places=0)
    nationality = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    Composers = models.Manager()

    def __str__(self):
        return self.last_name

