from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('home', views.home, name='home'),
    path('allshows', views.allshows, name='allshows'),  # allshows = entries
    path('<int:pk>/details/', views.details, name="details"),
    path('<int:pk>/delete/', views.delete, name="delete"),
    path('<int:pk>/edit/', views.edit, name="edit"),
    path('create/', views.create, name="create"),
]


