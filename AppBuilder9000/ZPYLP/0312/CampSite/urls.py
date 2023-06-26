from django.urls import path
from . import views


urlpatterns = [
    path('', views.campsite_home, name='CampSite_home'),
    path('add_campsite/', views.add_campsite, name='add_campsite'),
    path('browse_campsites/', views.browse, name='browse'),
    path('campsite_details/<int:campsite_id>/', views.campsite_details, name='campsite_details'),
    path('campsite_details/<int:campsite_id>/edit', views.edit_campsite, name='edit_campsite'),
    path('campsite_details/<int:campsite_id>/delete', views.delete_campsite, name='delete_campsite'),
    path('CampSite_nationalForest/', views.bs_scrape, name='nationalForest'),
    path('CampSite_searchAPI/', views.search_api, name='searchAPI'),
]
