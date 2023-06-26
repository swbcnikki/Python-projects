from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('SharksApp_home', views.SharksApp_home, name="SharksApp_home"),
    path('SharksApp_newitem/', views.Create_Shark, name="SharksApp_newitem"),
    path('SharksApp_displaydb/', views.Display_DB, name="SharksApp_displaydb"),
    path('<int:pk>/SharksApp_detailspage/', views.Shark_Details, name="SharksApp_detailspage"),
    path('<int:pk>/SharksApp_editpage/', views.Edit_Shark, name="SharksApp_editpage"),
    path('<int:pk>/SharksApp_deletepage/', views.Delete_Shark, name="delete"),
]
