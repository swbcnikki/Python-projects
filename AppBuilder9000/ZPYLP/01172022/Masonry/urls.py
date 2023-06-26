from django.urls import path
from . import views

urlpatterns = [
    path('', views.masonry_home, name='masonry_home'),
    path('Create/', views.createQuote, name='createQuote'),
    path('quote_view/', views.quote_view, name="All_quotes"),
    path('<int:pk>/details/', views.details, name="masonry_details"),
    path('<int:pk>/delete/', views.delete, name="delete"),
    path('confirmdelete', views.confirmed, name="confirmed"),
    path('Gallery', views.gallery, name="Gallery"),

]