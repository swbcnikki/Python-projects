from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.urls import path
from . import views


# you invoke the name while the views.'method' page occurs on your browser
urlpatterns = [
    path('', views.eurotriphome, name="ethome"),
    path('eastern/', views.eastern_list, name="eastern"),
    path('easternlocationscreate/', views.easternlocationscreate, name="easternlocationscreate"),
    path('eurotripdetails/<int:pk>/', views.eurotripdetails, name="eurotripdetails"),
    path('etedit/<int:pk>/', views.etedit, name="etedit"),
    path('etdelete/<int:pk>/', views.etdelete, name="etdelete"),
    path('currency/', views.currency, name="currencyconverter")
   ]



