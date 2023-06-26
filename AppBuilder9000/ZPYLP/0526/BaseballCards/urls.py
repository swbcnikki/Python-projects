from django.urls import path
from . import views

urlpatterns = [
    path('', views.cards_home, name='BaseballCards_home'),
    path('add/', views.add_card, name='BaseballCards_add'),
    path('catalog/', views.catalog, name='BaseballCards_catalog'),
    path('<int:pk>/details/', views.details, name='BaseballCards_details'),
]
