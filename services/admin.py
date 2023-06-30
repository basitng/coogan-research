from django.contrib import admin

from services.models import VideoFile


class VideoUploadModel(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(VideoFile)
