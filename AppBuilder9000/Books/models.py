from django.db import models

BOOK_GENRE = [
    ('Science-Fiction', 'Science-Fiction'),
    ('Action and Adventure', 'Action and Adventure'),
    ('Fantasy', 'Fantasy'),
    ('History', 'History'),
    ('Horror', 'Horror'),
    ('Comic Book', 'Comic Book'),
    ('Mystery', 'Mystery'),
    ('Poetry', 'Poetry'),
]

BOOK_RATING = [
    ('1/5', '1/5'),
    ('2/5', '2/5'),
    ('3/5', '3/5'),
    ('4/5', '4/5'),
    ('5/5', '5/5'),
]


# instantiating my model
class AddBook(models.Model):
    book_genre = models.CharField(max_length=20, choices=BOOK_GENRE)
    book_title = models.CharField(max_length=100, null=False)
    book_author = models.CharField(max_length=100, null=False)
    book_description = models.CharField(max_length=100, null=False)
    book_rating = models.CharField(max_length=20, choices=BOOK_RATING)

    objects = models.Manager()

    def __str__(self):
        return self.book_title


class FavoriteBook(models.Model):
    Title = models.CharField(max_length=100, null=False)
    Author = models.CharField(max_length=100, null=False)
    Rating = models.CharField(max_length=100, null=False)
    Source = models.CharField(max_length=100, null=False)

    Favorite_Book = models.Manager()

    def __str__(self):
        return self.Title