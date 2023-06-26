"""RidleyVerse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from YTfeed import views

urlpatterns = [
    path('', views.YTfeedhome, name='YTfeed-home'),
    path('Add-Youtubers/', views.AddYoutubers, name='Add-Youtubers'),
    path('List-Youtubers/', views.ListYoutubers, name='List-Youtubers'),
    path('<id>/update/', views.EditYoutubers, name='Update'),
    path('<id>/delete/', views.DeleteYoutubers, name='Delete'),
    path('<id>/Feed-Me/', views.FeedMe, name='Feed-Me'),
    path('<id>/View-Youtubers/', views.GetYTSoup, name='View-Youtubers')
]
