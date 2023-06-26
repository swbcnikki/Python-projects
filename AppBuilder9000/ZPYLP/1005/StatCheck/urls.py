from django.urls import path
from . import views
from .views import player_display

urlpatterns =[
    path('', views.StatCheckHome, name='StatCheckHome'),
    path('StatCheckPlayer', views.CheckPlayer, name='StatCheckPLAYER'),
    path('StatCheckTeam', views.CheckTeam, name='StatCheckTEAM'),
    path('StatCheckDisplay', views.player_display, name='StatCheckDISPLAY'),
    path('StatCheckDETAIL/<int:pk>/', views.CheckDetail, name='StatCheckDETAIL'),
]