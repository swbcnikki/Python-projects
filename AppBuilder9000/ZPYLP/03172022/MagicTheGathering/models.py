from django.db import models


TYPE_CHOICES = [
    ('General','General'),
    ('Standard','Standard'),
    ('Modern','Modern'),
    ('Legacy','Legacy'),
    ('Vintage','Vintage'),
    ('Commander','Commander'),
]

class Collection(models.Model):
    collection_name = models.CharField(max_length=50)
    collection_type = models.CharField(max_length=60, choices=TYPE_CHOICES)

    Collection = models.Manager()

    def __str__(self):
        return self.collection_name+''+self.collection_type

CARD_COLOR = [
    ('White','White'),
    ('Blue','Blue'),
    ('Black','Black'),
    ('Red','Red'),
    ('Green','Green'),
    ('Multi','Multi'),
    ('Colorless','Colorless'),
]

CARD_TYPE = [
    ('Creature','Creature'),
    ('Instant','Instant'),
    ('Sorcery','Sorcery'),
    ('Land','Land'),
    ('Enchantment','Enchantment'),
    ('Artifact','Artifact'),
    ('Plainswalker','Plainswalker'),
]

class Card(models.Model):
    card_name = models.CharField(max_length=50)
    card_color = models.CharField(max_length=10, choices=CARD_COLOR)
    card_cost = models.CharField(max_length=10)
    card_type = models.CharField(max_length=15, choices=CARD_TYPE)
    card_text = models.CharField(max_length=250)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

    Cards = models.Manager()

    def __str__(self):
        return self.card_name

