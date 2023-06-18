# urls.py
from django.urls import path
from .views import VideoUploadView

urlpatterns = [
    path('audio/', VideoUploadView.as_view(), name='audio-file'),
]
