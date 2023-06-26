from django.urls import path


from .import views

urlpatterns = (
    path('', views.ComBooks, name='ComicBooks_home'),
    path('ComicBooks_forsale', views.forSale, name='ComicBooks_forsale'),
    path('ComicBooks_index', views.ComIndex, name='ComicBooks_index'),
    path('Cominfo/<int:pk>/', views.Cominfo, name='Cominfo'),

)
