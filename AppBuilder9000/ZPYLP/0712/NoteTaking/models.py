from django.db import models

# Create your models here.

PRIORITY_CHOICE = (
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High')
)

class Categorie(models.Model):
    Name = models.CharField(max_length=50, null=False)

    object = models.Manager()

    def __str__(self):
        return self.Name

class Note(models.Model):
    Title = models.CharField(max_length=50, null=False)
    Category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    Details = models.TextField(max_length=300, default="", blank=True)
    Priority = models.CharField(max_length=50, default="", choices=PRIORITY_CHOICE)

    object = models.Manager()

    def __str__(self):
        return self.Title

