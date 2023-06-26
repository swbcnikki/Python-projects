from django.db import models
from django.urls import reverse



# need a book model to track the books
class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250, null=True)
    # read allows lists to be created with the books
    # if read = true then it goes on the read list
    # if read = false then it goes on the wishlist
    read = models.BooleanField(null=True)
    comments = models.TextField(null=True)
    image = models.URLField(max_length=250, null=True)

    # objects manager
    objects = models.Manager()

    # create url absolute path for each book
    def get_absolute_url(self):
        return reverse('BookClubApp_book', args=[str(self.pk)])

    # authors returned from the api can be a list, so this method splits them by quotation marks
    def authors_as_list(self):
        return self.author.split('\'')

    # References to the books are returned as the book title
    # instead of the primary key
    def __str__(self):
        return self.title


