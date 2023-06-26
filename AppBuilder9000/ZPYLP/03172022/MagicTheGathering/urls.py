from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.MagicTheGathering_home, name='MagicTheGathering_home'),
    path('MagicTheGathering_API/', views.MagicTheGathering_API, name='MagicTheGathering_API'),
    path('create/', views.create_collection, name='create'),
    path('add/', views.create_card, name='add'),
    path('collection/>', views.collection, name='collection'),
    path('<int:pk>/Card_details/', views.details, name='Card_details'),
    path('<int:pk>/editCardInfo/', views.editCardInfo, name='editCardInfo'),
    path('<int:pk>/delete_card/', views.delete_card, name="delete_card"),
    path('How_Too/', views.How_Too, name="How_Too"),
    ]