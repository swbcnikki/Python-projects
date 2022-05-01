from django.contrib import admin

# Register your models here.
from .models import djangoClasses, prereq, book

#registration of the models
admin.site.register(djangoClasses)
admin.site.register(prereq)
admin.site.register(book)
