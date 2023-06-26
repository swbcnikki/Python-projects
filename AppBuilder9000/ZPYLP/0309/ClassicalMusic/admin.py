from django.contrib import admin

from .models import Musician
from .models import Role
from .models import Composition
from .models import Movement
from .models import Track
from .models import Release

# Register your models here.
admin.site.register(Musician)
admin.site.register(Role)
admin.site.register(Composition)
admin.site.register(Movement)
admin.site.register(Track)
admin.site.register(Release)
