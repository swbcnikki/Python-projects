
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.study_home, name='study_home'),
    path('<int:pk>/info/', views.info, name='info'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('register/', views.sign_up, name='sign_up'),
    path('diary/', views.diary, name='diary'),
    path('login/',  views.login, name='login'),
    path('members/',  views.members, name='members'),
    path('focus/', views.focus, name='focus'),
    path('activity/', views.activity, name='activity'),
]