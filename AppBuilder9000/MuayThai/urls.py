from . import views
from django.urls import path


# the directory of . is our current directory
# so the above says import views.py from the current directory
# ANATOMY OF A URL ROUTE:
# ('pattern to watch for',method to call,"shortcut name")
# uses "name= " to link in document.

urlpatterns = [
    path('', views.Muay_Thai_Home, name='MuayThai_home'),  # usable link to home page
    path('FighterEntry/', views.MuayThai_fighter_entry, name='MuayThai_fighter_entry'),  # usable link to create page
    path('DisplayFighters/', views.MuayThai_display_fighters, name='MuayThai_display_fighters'),  # link to display fighter's names
    path('<int:pk>/details/', views.MuayThai_fighters_details, name='MuayThai_fighter_details'),  # link to detail of fighters
    path('<int:pk>/delete_fighter/', views.MuayThai_delete_fighter, name='MuayThai_delete'),
    path('confirm_delete/', views.MuayThai_delete, name='MuayThai_confirm_delete'),
    path('BetsApi', views.MuayThai_fighters_api, name="MuayThai_fighters_api"),
    path('MuayThai_beautifulSoup', views.MuayThai_soup, name="MuayThai_beautifulSoup"),
]
