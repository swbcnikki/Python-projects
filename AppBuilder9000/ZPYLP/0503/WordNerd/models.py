from django.db import models
#add model word that takes in 4 different fields
class word(models.Model):
    word_name = models.CharField(max_length=75)
    word_definition = models.CharField(max_length=255)
    word_in_a_sentence = models.CharField(max_length=255)
    where_did_you_find_the_word = models.CharField(max_length=255, null=True)
    parent_languages = models.CharField(max_length=255, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.word_name





