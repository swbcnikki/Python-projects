from django.db import models


TYPE_CHOICES = {
    ('appetizers', 'appetizers'),
    ('soups', 'soups'),
    ('entrees', 'entrees'),
    ('desserts', 'desserts'),
    ('beverages', 'beverages'),
}


class Food(models.Model):
    type = models.CharField(max_length=12, choices=TYPE_CHOICES)
    name = models.CharField(max_length=60, default="", blank=True, null=False)
    servings = models.IntegerField(default=0)
    recipe = models.TextField(max_length=1000, default="", blank=True)
    dateSubmitted = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return self.name
