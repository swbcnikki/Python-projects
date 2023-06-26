from django.contrib import admin
from .models import MusicalArtists
from .models import SongNames
from .models import AlbumNames


# Register your models here.
admin.site.register(MusicalArtists)
admin.site.register(SongNames)
admin.site.register(AlbumNames)
