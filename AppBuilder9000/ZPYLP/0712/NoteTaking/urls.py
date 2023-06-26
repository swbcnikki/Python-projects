from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='NoteTaking_home'),
    path('AddNotes/', views.AddNotes, name='NoteTaking_addnotes'),
    path('AddCategories/', views.AddCategories, name='NoteTaking_addcategories'),
    path('<int:pk>/Details/', views.Details, name="NoteTaking_details"),
    path('<int:pk>/Delete/', views.DeleteNotes, name="NoteTaking_confirmdelete"),
    path('Suggestion/', views.SuggestionsAPI, name="NoteTaking_suggestions")
]
