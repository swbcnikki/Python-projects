from django.db import models

# Choices for plant type selector
TYPE_CHOICES = (
    ('Fruit', 'Fruit'),
    ('Vegetable', 'Vegetable'),
    ('Herb', 'Herb'),
    ('Flower', 'Flower'),
    ('Tree', 'Tree'),
    ('Shrub','Shrub'),
)
# Choices for season planted selector
SEASON_CHOICES = (
    ('Spring', 'Spring'),
    ('Summer', 'Summer'),
    ('Fall', 'Fall'),
    ('Winter', 'Winter'),
)

# Main Garden Planner model
class Plants(models.Model):
    name = models.CharField(max_length=75)
    type = models.CharField(choices=TYPE_CHOICES, max_length=120)
    season_planted = models.CharField(choices=SEASON_CHOICES, max_length=120)
    date_planted = models.DateField()
    days_to_harvest = models.IntegerField()

    def __str__(self):
        return self.name

    objects = models.Manager()

