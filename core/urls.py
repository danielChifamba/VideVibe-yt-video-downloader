from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('VideVibe/download_info/', views.download, name="download"),
    path('VideVibe/about_us/', views.about, name="about"),
    path('VideVibe/download_media/<format_type>/', views.completeDownload, name="completeDownload")
]