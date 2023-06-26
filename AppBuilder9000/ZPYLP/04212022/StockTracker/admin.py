from django.contrib import admin
from .models import StockData, StockUser, StockHolderCompany

admin.site.register(StockData)
admin.site.register(StockUser)
admin.site.register(StockHolderCompany)
