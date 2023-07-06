# urls.py
from django.urls import path
from .views import GetVideo, VideoUploadView, GenerateMidjourneyImage

urlpatterns = [
    path('video/', VideoUploadView.as_view(), name='audio-file'),
    path('imagine/', GenerateMidjourneyImage.as_view(), name='imagine-file'),
    path('', GetVideo.as_view(), name=''),
]
