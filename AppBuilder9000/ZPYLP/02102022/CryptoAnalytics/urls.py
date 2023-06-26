from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='crypto_home'),
    path('register', views.register, name='crypto_register'),
    path('login', views.login_page, name='crypto_login'),
    path('about', views.about, name='crypto_about'),
    path('display', views.crypto_display, name='crypto_display'),
    path('details/<int:pk>', views.crypto_details, name='crypto_details'),

]
