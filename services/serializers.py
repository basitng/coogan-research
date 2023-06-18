# serializers.py
from rest_framework import serializers
from .models import VideoFile


class VideoFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoFile
        fields = ('id', 'video_url', 'transcript')
