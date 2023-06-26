from django.contrib import admin
from .models import Song, Playlist


# Register your models here.
# registering the models here allows me to use the admin page to test the templates functionality.
admin.site.register(Song)
admin.site.register(Playlist)
