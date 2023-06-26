from django.urls import path
from . import views
from django.http import HttpResponse


urlpatterns = [
    path('', views.home, name='MusicApp_home'),
    path('create_artist/', views.MusicApp_create_artist, name='MusicApp_create_artist'),
    path('create_song/', views.MusicApp_create_song, name='MusicApp_create_song'),
    path('create_album/', views.MusicApp_create_album, name='MusicApp_create_album'),
    path('artist/Index/', views.artist_index, name='MusicApp_artist_index'),
    path('song/Index/', views.song_index, name='MusicApp_song_index'),
    path('album/Index', views.album_index, name='MusicApp_album_index'),
    path('artist/Search', views.artist_search_results, name='MusicApp_artist_search_results'),
    path('song/Search', views.song_search_results, name='MusicApp_song_search_results'),
    path('album/Search', views.album_search_results, name='MusicApp_album_search_results'),
    path('artist/<int:pk>/Details/', views.artist_details, name='MusicApp_artist_details'),
    path('song/<int:pk>/Details/', views.song_details, name='MusicApp_song_details'),
    path('album/<int:pk>/Details/', views.album_details, name='MusicApp_album_details'),
    path('artist/<int:pk>/Edit/', views.edit_artist, name='MusicApp_edit_artist'),
    path('song/<int:pk>/Edit/', views.edit_song, name='MusicApp_edit_song'),
    path('album/<int:pk>/Edit/', views.edit_album, name='MusicApp_edit_album'),
    path('artist/<int:pk>/Delete/', views.delete_artist, name='MusicApp_delete_artist'),
    path('song/<int:pk>/Delete/', views.delete_song, name='MusicApp_delete_song'),
    path('album/<int:pk>/Delete/', views.delete_album, name='MusicApp_delete_album'),
    path('artists_chart', views.bs_artist_chart, name='MusicApp_top_artists_chart'),
]
