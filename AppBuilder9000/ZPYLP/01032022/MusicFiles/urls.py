from django.urls import path
from . import views


urlpatterns = [
    path('', views.musicfiles_home, name='musicfiles_home'),
    path('create', views.musicfiles_create, name="Create"),
    path('list', views.all_files_view, name='all_files'),
    path('<int:pk>/fileDetails', views.musicFileDetails, name="musicfiles_details"),
]