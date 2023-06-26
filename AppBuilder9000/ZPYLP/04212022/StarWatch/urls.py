from django.urls import path
from . import views

urlpatterns = [
    path('', views.StarWatch_home, name='StarWatch_home'),
    path('StarWatch_addObject/', views.add_object, name='StarWatch_addObject'),
    path('StarWatch_listObjects/', views.list_objects, name='StarWatch_listObjects'),
    path('<int:pk>/StarWatch_objectDetails/', views.object_details, name='StarWatch_objectDetails'),
    path('StarWatch_filterPlanets/', views.list_planets, name='StarWatch_filterPlanets'),
    path('StarWatch_filterStars/', views.list_stars, name='StarWatch_filterStars'),
    path('StarWatch_filterMoons/', views.list_moons, name='StarWatch_filterMoons'),
    path('StarWatch_filterOther/', views.list_other, name='StarWatch_filterOther'),
    path('<int:pk>/StarWatch_editObject/', views.edit_object, name='StarWatch_editObject'),

    path('<int:pk>/StarWatch_deleteObject/', views.delete_object, name="StarWatch_deleteObject"),
]

