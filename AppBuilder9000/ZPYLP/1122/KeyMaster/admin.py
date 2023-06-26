from django.contrib import admin

# Register your models here.
from .models import Games
admin.site.register(Games)

from .models import Dlc
admin.site.register(Dlc)

from .models import Wishlist
admin.site.register(Wishlist)