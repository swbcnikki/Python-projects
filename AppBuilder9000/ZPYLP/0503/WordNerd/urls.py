from django.urls import path
from .import views
# The url name is used to redirected the user via views.py to the url path
urlpatterns = [
    path('', views.WordNerd_home, name='WordNerd_home'),
    path('WordNerd_createword/', views.WordNerd_createword, name='WordNerd_createword'),
    path('WordNerd_viewdata/', views.WordNerd_viewdata, name='WordNerd_viewdata'),
    path('<int:pk>/WordNerd_worddetails/', views.WordNerd_worddetails, name="WordNerd_worddetails"),
    path('<int:pk>/WordNerd_wordupdate/', views.WordNerd_wordupdate, name="WordNerd_wordupdate"),
    path('<int:pk>/WordNerd_worddelete/', views.WordNerd_worddelete, name="WordNerd_worddelete"),
]
