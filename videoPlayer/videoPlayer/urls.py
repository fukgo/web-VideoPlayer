"""
URL configuration for videoPlayer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.urls import re_path

from video import views

urlpatterns = [
    path('video/<str:file_path>', views.stream_video, name='stream_video'),
    path('video_list/', views.video_list, name='video_list'),
    path('dplayer/<str:file_path>', views.dplayer, name='dplayer'),
    path('video_list_2/', views.video_list_2, name='video_list_2'),
    re_path(r'^.*$', views.index, name='index'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
