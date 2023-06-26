from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='MarketWatch_home'),
    path('AccountPage/', views.account, name='Account'),
    path('Listview/', views.all_webscrape, name='Listview'),
    path('DetailView/<int:pk>', views.detailsview, name='DetailView'),
]