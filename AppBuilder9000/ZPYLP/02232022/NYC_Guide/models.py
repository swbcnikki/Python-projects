from django.db import models

# to lessen errors in spelling for later search features
BoroughType= [('Manhattan', 'Manhattan'), ('Brooklyn', 'Brooklyn'), ('Queens', 'Queens'), ('Staten Island', 'Staten Island'), ('Bronx', 'Bronx')]


# to lessen errors in spelling for later search features
CuisineType= [('Italian', 'Italian'), ('American', 'American'), ('Asian Fusion', 'Asian Fusion'), ('Bar', 'Bar'),
              ('BBQ', 'BBQ'), ('French', 'French'), ('Greek', 'Greek'), ('Mediterranean', 'Mediterranean'), ('Mexican', 'Mexican'), ('Pizza', 'Pizza'),
              ('Seafood', 'Seafood'), ('Southern Food', 'Southern Food'), ('Japanese', 'Japanese'), ('Chinese', 'Chinese')]

# to lessen errors in spelling for later search features
PriceRange= [('$', '$'), ('$$', '$$'), ('$$$', '$$$'), ('$$$$', '$$$$')]

class Restaurants(models.Model):
    restaurant_name= models.CharField(max_length=75)
    cuisine = models.CharField(max_length=100, choices=CuisineType)
    borough= models.CharField(max_length=100, choices= BoroughType)
    neighborhood= models.CharField(max_length=75)
    price_range= models.CharField(max_length=100, choices= PriceRange)
    address=models.CharField(max_length=225)
    state= models.CharField(max_length=100)
    zip_code= models.IntegerField()

    Restaurants= models.Manager()

    def __str__(self):
        return self.restaurant_name