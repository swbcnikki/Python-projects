
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IceHockey_home, name='IceHockey_home'),
    path('newprofile', views.IceHockey_newprofile, name='IceHockey_newprofile'),
    path('<int:pk>/allprofiles', views.IceHockey_allprofiles, name='IceHockey_allprofiles'),
    path('<int:pk>/myprofile', views.IceHockey_myprofile, name='IceHockey_myprofile'),
    path('<int:pk>/details/', views.IceHockey_details, name='IceHockey_details'),
    path('<int:pk>/edit/', views.IceHockey_edit, name='IceHockey_edit'),
    path('<int:pk>/delete/', views.IceHockey_delete, name='IceHockey_delete'),
    path('<int:pk>/scrapeddata/', views.IceHockey_scrapeddata, name='IceHockey_scrapeddata'),
    path('samplescrape', views.IceHockey_samplescrape, name='IceHockey_samplescrape'),
    path('sampleapi', views.IceHockey_sampleapi, name='IceHockey_sampleapi'),
    path('<int:pk>/api_page', views.IceHockey_api_page, name='IceHockey_api_page'),
    path('<int:pk>/error', views.IceHockey_error, name='IceHockey_error'),
    path('<int:pk>/fav_add', views.IceHockey_fav_add, name='IceHockey_fav_add'),
    path('<int:pk>/confirm_add', views.IceHockey_confirm_add, name='IceHockey_confirm_add'),
    path('<int:pk>/show_favorites', views.IceHockey_show_favorites, name='IceHockey_show_favorites'),
    path('register', views.IceHockey_register, name='IceHockey_register'),
    path('login', views.IceHockey_login_request, name='IceHockey_login'),
    path('logout', views.IceHockey_logout_request, name='IceHockey_logout'),
    path('<int:pk>/api_choice', views.IceHockey_api_choice, name='IceHockey_api_choice')
]