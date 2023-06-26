from django.contrib import admin
from .models import Motorcycle
from .models import Route

# Registered my model
admin.site.register(Motorcycle)
admin.site.register(Route)
