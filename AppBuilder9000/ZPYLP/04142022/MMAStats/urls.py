from django.urls import path
from django.conf import settings
from django.conf.urls import url, include
from . import views
from django.conf.urls.static import static

# **<int:pk> says that we should expect a pk(primary key) in the url
urlpatterns = [
    path('', views.MMAHome, name='MMA_Home'),
    path('create/', views.MMACreate, name='MMA_Create'),
    path('stats/', views.DisplayStats, name='MMA_Stats'),
    path('events/', views.EventScrape, name='MMA_Events'),
    path('details/<int:pk>', views.DisplayDetails, name='MMA_Details'),
    path('delete/<int:pk>', views.DeleteStat, name="MMA_Delete"),
    path('update/<int:pk>', views.UpdateStat, name="MMA_Update")

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)