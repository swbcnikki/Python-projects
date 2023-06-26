from django.db import models

# provides drop down on adding exercises
TARGET_MUSCLE_CHOICES = (
    ('Chest','Chest'),
    ('Back','Back'),
    ('Legs','Legs'),
    ('Shoulders','Shoulders'),
    ('Arms','Arms'),
)

# this is the model for everything that gets entered into the database
class Exercises(models.Model):
    target_muscle = models.CharField(max_length=60, choices=TARGET_MUSCLE_CHOICES)
    exercise_name = models.CharField(max_length=60, default="", blank=True, null=False)
    repetitions = models.CharField(max_length=20, default="", blank=True, null=False)
    sets = models.CharField(max_length=20, default="", blank=True, null=False)
    description = models.TextField(max_length=500, default="", blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.exercise_name




