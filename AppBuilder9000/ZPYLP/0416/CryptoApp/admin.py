from django.contrib import admin

from .models import Currency, CoinStatus

# Don't need this yet.
#class CurrencyAdmin(admin.ModelAdmin):
#    fields = []

# To register multiple models at once, must enter as iterable list
admin.site.register([Currency, CoinStatus])

