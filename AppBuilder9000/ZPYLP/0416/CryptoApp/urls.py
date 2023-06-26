from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='CryptoApp_home'),
    path('create/', views.add_currency, name='CryptoApp_AddCurrency'),
    path('update/', views.add_status, name='CryptoApp_AddStatus'),
    path('display/', views.display, name='CryptoApp_display'),
    path('details/<int:record_id>/', views.details, name='CryptoApp_details'),
    path('edit/<int:record_id>/', views.edit, name='CryptoApp_edit'),
    path('update/<int:record_id>/', views.update, name='CryptoApp_update'),
    path('delete/<int:record_id>/', views.delete, name='CryptoApp_delete'),
    path('trending/', views.trending, name='CryptoApp_trending'),
    path('lookup/', views.lookup, name='CryptoApp_lookup'),
    path('lookup/results/', views.results, name='CryptoApp_results'),
]
