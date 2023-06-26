# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.conf.urls import include
# from django.contrib import admin
# Comment-in above lines as-needed
from django.urls import path
from . import views


urlpatterns = [ # stores the routes/paths within the project; the 'WHEN' what's in'PasswordManager/templates/views.py' gets displayed
    path('', views.home, name='PwdMgr_home'),
    path('passwordInput/', views.passwordInput, name='PwdMgr_pwdInput'),
    path('passwordsList/', views.passwordsList, name='PwdMgr_pwdsList'),
    path('details/<int:id>/', views.passwordDetails, name='PwdMgr_details'),
]