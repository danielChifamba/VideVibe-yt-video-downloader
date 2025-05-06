from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('VidVibe/download_info/', views.download, name="download"),
    path('VidVibe/about_us/', views.about, name="about"),
    path('VidVibe/download_media/<format_type>/', views.completeDownload, name="completeDownload")
]
