from django.db import models
from .fields import IngredientMultiField


class IngredientMultiModelField(models.Field):

    def formfield(self, **kwargs):
        defaults = {'form_class': IngredientMultiField}
        defaults.update(kwargs)
        return super(IngredientMultiModelField, self).formfield(**defaults)

    def get_internal_type(self):
        return 'TextField'


class Cocktail(models.Model):
    cocktail_name = models.CharField(max_length=50, unique=True)
    ingredient_1 = IngredientMultiModelField(blank=True)
    ingredient_2 = IngredientMultiModelField(blank=True)
    ingredient_3 = IngredientMultiModelField(blank=True)
    ingredient_4 = IngredientMultiModelField(blank=True)
    ingredient_5 = IngredientMultiModelField(blank=True)
    ingredient_6 = IngredientMultiModelField(blank=True)
    ingredient_7 = IngredientMultiModelField(blank=True)
    ingredient_8 = IngredientMultiModelField(blank=True)
    ingredient_9 = IngredientMultiModelField(blank=True)
    description = models.TextField()
    directions = models.TextField()
    avg_rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    # photo = models.FileField(upload_to='static/CocktailRecipes/user_images', blank=True)

    Cocktails = models.Manager()

    def __str__(self):
        return str(self.cocktail_name)


rating_choices = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]


class Review(models.Model):
    user_name = models.CharField(max_length=50)
    rating = models.PositiveSmallIntegerField()
    comments = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)

    Reviews = models.Manager()
