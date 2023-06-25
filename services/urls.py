# urls.py
from django.urls import path
from .views import GetVideo, VideoUploadView

urlpatterns = [
    path('video/', VideoUploadView.as_view(), name='audio-file'),
    path('vid/', GetVideo.as_view(), name=''),
]
