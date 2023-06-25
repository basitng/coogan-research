# models.py
from django.db import models


class VideoFile(models.Model):
    video_url = models.CharField(max_length=1)
    transcript = models.TextField(blank=True)
