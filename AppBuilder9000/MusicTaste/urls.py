from django.urls import path
from . import views

urlpatterns = [
    path('', views.musictaste_home, name='MusicTaste_home'),
    path('test/', views.registerform, name='test'),
    path('<int:pk>/details/', views.userdetails, name='Music_User_Details'),
    path('MusicDisplay/', views.displayusers, name='Music_Display'),
]
