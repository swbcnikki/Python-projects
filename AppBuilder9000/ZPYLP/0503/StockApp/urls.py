from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='StockApp_home'),
    path('StockApp_base/', views.base, name='StockApp_base'),
    path('StockApp_newstock/', views.new, name='StockApp_newstock'),
    path('StockApp_Watchlist/', views.watchlist, name='StockApp_Watchlist'),
    path('<int:pk>/StockApp_Details/', views.details, name='StockApp_Details'),
    path('<int:pk>/StockApp_confirm/', views.confirm, name="StockApp_confirm"),
    path('<int:pk>/StockApp_edit/', views.edit, name='StockApp_edit'),

]


