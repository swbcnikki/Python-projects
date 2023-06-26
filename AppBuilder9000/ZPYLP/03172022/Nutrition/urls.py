from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
#this addition gives access to the 'include()' function that we use below in urlpatterns
from django.contrib import admin
from django.urls import path
from . import views #the directory of . is our current directory
#so the above says import views.py from the current directory
#ANATOMY OF A URL ROUTE:
#('pattern to watch for',method to call,"shortcut name")
urlpatterns = [

    path('', views.nutrition_home, name="Nutrition_home"),
    path('create_account/', views.create_account, name='create_account'),
    path('make_query/', views.make_query, name='make_query'),
    path('display_db', views.display_db, name="display_db"),
    path('scraper', views.scraper, name="scraper"),
    path('<int:pk>/display_account_details/', views.display_account_details, name="display_account_details"),#call display_details() and pass in pk
    path('<int:pk>/display_nutrition_details/', views.display_nutrition_details, name="display_nutrition_details"),
    path('<int:pk>/delete_account/', views.delete_account, name="delete_account"),
    path('<int:pk>/delete_nutrition/', views.delete_nutrition, name="delete_nutrition"),
    path('<int:pk>/edit_account/', views.edit_account, name="edit_account"),
    path('<int:pk>/edit_nutrition/', views.edit_nutrition, name="edit_nutrition"),
    path('scraper/', views.scraper, name="scraper"),
    path('nutritionix_nutrients_api/', views.nutritionix_nutrients_api, name="nutritionix_nutrients_api"),
    path('save_nutritionix_nutrients_api', views.save_nutritionix_nutrients_api, name="save_nutritionix_nutrients_api"),


]
    #when it sees name="nutrition_home" it knows to go to the views.createRecord method and
    #change the name of the URL to include nutrition_home