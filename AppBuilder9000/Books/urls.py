from django.urls import path
from . import views

# urls which point to function in views.py
urlpatterns = [
    path('', views.books_home, name='books_home'),
    path('AddBook/', views.books_add_book, name='books_add_book'),
    path('Reviews/', views.books_reviews, name='books_reviews'),
    path('<int:pk>/Details/', views.books_details, name='books_details'),
    path('<int:pk>/Delete/', views.books_delete, name='books_delete'),
    path('<int:pk>/Update/', views.books_update, name='books_update'),
    path('BookAPI/', views.books_api, name='books_api'),
    path('Favorites', views.books_fav, name='books_fav'),
    path('ViewFavorites', views.view_fav_books, name='view_fav_books'),
]
