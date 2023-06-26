from django.urls import path
from . import views


urlpatterns = [
    path('', views.hiphop_home, name='hiphop_home'),
    path('hiphop_create/', views.create_choose, name='hiphopviews_view'),
    path('all/', views.all_items, name='all_items'),
    path('<int:pk>/objects_id>/', views.hiphop_details, name='hiphop_details'),
]
