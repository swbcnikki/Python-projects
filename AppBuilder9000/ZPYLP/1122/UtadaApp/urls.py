from django.urls import path
from . import views

#urls for the website
urlpatterns = [
    path('',views.home,name='hiki_home'),
    path('music',views.music,name ='hiki_music'),
    path('entries', views.entries,name ='hiki_entries'),
    path('<int:pk>/submissions/',views.submissions, name='hiki_details'),
    path('<int:pk>/editer/',views.editer, name='hiki_edit'),
    path('<int:pk>/delete/',views.delete,name='hiki_delete')


]