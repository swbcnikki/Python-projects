from django.contrib import admin

from .models import Game, Image, Meetup

# Registering our models
admin.site.register(Game)

# 2 new objects for our Meetup API
class MeetupAdmin(admin.ModelAdmin):
    list_display =('admin_thumbnail', 'name', 'contact', 'location')
    list_display_links =('name',)
admin.site.register(Meetup, MeetupAdmin)

class ImageAdmin(admin.ModelAdmin):
    list_display = ('admin_thumbnail', 'name', 'image_url',)
    list_display_links = ('name',)
admin.site.register(Image, ImageAdmin)
