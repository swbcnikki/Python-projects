
from django.urls import path
from . import views

urlpatterns = [
    path('at_home', views.at_home, name='at_home'),
    path('add_song', views.add_song, name='add_song'),
    path('add_playlist', views.add_playlist, name='add_playlist'),
    path('library', views.at_library, name='at_library'),
    path('at_all_songs', views.at_all_songs, name='at_all_songs'),
    path('<int:pk>/details', views.at_details, name='at_details'),
    path('<int:pk>/delete', views.at_delete, name='at_delete'),
    path('<int:pk>/playlist_details', views.at_playlist_details, name='at_playlist_details'),
    path('<int:pk>/playlist_delete', views.at_playlist_delete, name='at_playlist_delete'),
    path('<int:pk>/lyrics', views.at_lyrics_api, name='at_lyrics_api'),
    path('<int:pk>/artist_info', views.at_artist_info, name='at_artist_info'),
]
