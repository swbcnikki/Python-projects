from . import views
from django.urls import path

urlpatterns = [
    path('', views.stock_home_page, name='stock_home'),
    path('StockAdd', views.stock_add_page, name='stock_add'),
    path('StockData', views.stock_display_database_page, name='stock_display_database'),
    path('<int:pk>/StockDetails', views.stock_details, name='stock_details')
]
