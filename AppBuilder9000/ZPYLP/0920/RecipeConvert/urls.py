from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="RecCon_home"),
    path("Convert/", views.convert, name="RecCon_convert"),
    path("list/", views.myrecipesList, name="RecCon_myrecipes"),
    path("details/<int:_id>/", views.details, name="RecCon_detail"),
]

# views.myrecipesList, name='RecCon_myrecipes'