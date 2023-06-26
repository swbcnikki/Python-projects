from django.urls import path
from . import views

urlpatterns = [
    path('', views.TVshow_home, name='TVshow_home'),
    path('addShow/', views.addShow, name='addShow'),
    path('seeShow/', views.seeShow, name='seeShow'),
    path('sortShow/', views.sortShow, name='sortShow'),
    path('sortGenre/', views.sortGenre, name='sortGenre'),
    path('showIndex/', views.showIndex, name='showIndex'),
    path('<int:pk>/showDetails/', views.showDetails, name='showDetails'),
]