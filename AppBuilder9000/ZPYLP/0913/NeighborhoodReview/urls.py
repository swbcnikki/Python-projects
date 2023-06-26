from django.conf.urls import include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.neighborhoodReview_home, name='NeighborhoodReview/NeighborhoodReview_home.html'),
    path('createneighborhood/', views.create_neighborhood, name='NeighborhoodReview/CreateNewNeighborhood.html'),
    path('review/', views.review, name='NeighborhoodReview/CreateReview.html'),
    path('<int:pk>/viewreviews/', views.reviewpage, name='NeighborhoodReview/ReviewPage.html'),
    path('neighborhood_details/', views.details, name='NeighborhoodReview/DisplayAllNeighborhoods.html'),
    path('<id>/neighborhood_item_details/', views.item_details, name='DisplayNeighborhood_item.html'),
    path('<int:pk>/edit_neighborhood/', views.edit_neighborhood, name='NeighborhoodReview/edit.html'),
    path('<int:pk>/DeleteNeighborhood/', views.delete_neighborhood, name='NeighborhoodReview/DeleteNeighborhood.html'),
    path('<id>/edit_review/', views.edit_review, name='NeighborhoodReview/edit_Review.html'),
    path('<id>/DeleteReview/',views.delete_review, name= 'NeighborhoodReview/DeleteReview.html'),
    path('Review_Details/',views.review_details, name= 'NeighborhoodReview/Review_Details.html'),
    path('<id>/review_item_detail/', views.review_item, name='Review_items.html'),
    path('soup_page/', views.soup_page, name="NeighborhoodReview/BeautifulSoup.html"),
    path('api/', views.api_pull, name ="NeighborhoodReview/API.html"),
    path('metro_inv_stats/', views.api_data, name ="NeighborhoodReview/Metro_Housing_Inventory_Data.html"),

]

