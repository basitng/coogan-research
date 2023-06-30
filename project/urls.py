from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('api-auth/', include('rest_framework.urls'), name='rest_framework'),
    path('admin/', admin.site.urls, name='admin'),
    path('', include('services.urls'), name='api')
]
