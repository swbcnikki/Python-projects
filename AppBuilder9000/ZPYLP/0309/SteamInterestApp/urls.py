
from django.urls import path
from . import views

urlpatterns = [
    path('', views.SIAHomePage, name='SIAHome'),
    path('AddEntry/', views.SIAAddEntry, name='SIAAddEntry'),
    path('EntrySuccess/', views.SIAAddConfirmation, name='SIAAddSuccess'),
    path('AllEntries/', views.SIAViewAll, name='SIAAllEntries'),
    path('<int:pk>/details/', views.SIAViewEntry, name='SIAEntry'),
    path('EditSuccess/', views.SIAEditConfirmation, name='SIAEditSuccess'),
    path('<int:pk>/deleteSuccess/', views.SIADeleteEntry, name='SIADeleteSuccess'),
    path('DataScrapeTest/', views.SIADataScrapeTest, name='SIADataScrapeTest'),
    path('<int:pk>/SteamAPITest/', views.SIASteamAPITest, name='SIASteamAPITest'),
    path('SteamGameIDEntry/', views.SIASteamGameIDEntry, name='SIASteamGameIDEntry'),
    ]
