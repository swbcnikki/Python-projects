from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="Novels_home"),
    path('Novels_create/', views.novelEntry, name="Novels_create"),
    path('Novels_display/', views.novelDisplay, name="Novels_display"),
    path('<int:pk>/Novels_details/', views.novelDetails, name="Novels_details"),
    path('<int:pk>/Novels_delete/', views.novelDelete, name="Novels_delete"),
    path('Novels_define/', views.defineWord, name="Novels_define"),
    path('Novels_why/', views.soupRead, name="Novels_why"),
    path('test/', views.github, name='test'),
]