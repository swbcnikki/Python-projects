from django.contrib import admin

# Register your models here.
from .models import djangoClasses

#registration of the models
admin.site.register(djangoClasses)

