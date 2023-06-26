from django.db import models

# Create your models here.
item_type = (
    ('recipe', 'recipe'),
    ('tool', 'tool'),
    ('furniture', 'furniture'),
    ('wallpaper', 'wallpaper'),
    ('flooring', 'flooring'),
    ('art', 'art'),
    ('fossil', 'fossil'),
    ('fish', 'fish'),
    ('bugs', 'bugs'),
)


class Item(models.Model):
    item_type = models.CharField(max_length=60, choices=item_type)
    name = models.CharField(max_length=60, default="", blank=True, null=False)
    amount = models.CharField(max_length=20, default="", blank=True, null=False)

    Items = models.Manager()

    def __str__(self):
        return self.name


