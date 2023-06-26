from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blogs'),
    path('Add/', views.Add, name='EntryPage'),
    path('Display/', views.Display, name='DisplayPage'),
    path('postdetails/<int:pk>/Details/', views.post_details, name='DetailsPage'),
    path('editpost/<int:pk>/Edit/', views.edit_post, name='EditPage'),
    path('deletepost/<int:pk>/Delete/', views.delete_post, name='DeletePage'),
]
