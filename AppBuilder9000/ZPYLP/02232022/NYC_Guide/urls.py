from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='nyc_guide_home'),
    path('add/', views.add_rest, name='add_rest'),
    path('all/', views.all_rest, name='all_rest'),
    path('<int:restaurants_id>/', views.details, name='details'),
    path('search/', views.search_rest, name='search'),
    path('update/<int:restaurants_id>', views.update_rest, name='update'),
    path('delete/<int:restaurants_id>', views.delete, name='delete'),
    path('yelp', views.yelp, name='yelp'),
]