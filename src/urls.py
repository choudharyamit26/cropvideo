from django.urls import path
from .views import CropVideo

app_name = "src"

urlpatterns = [
    path('crop-video/', CropVideo.as_view(), name="crop-video")
]
