from django.urls import path

from . import views
from .views import FaceImage, FaceImageDisplay

app_name = 'facerecognition'

urlpatterns = [
    # ex: /polls/
    #path('', views.index, name='index'),
    path('', FaceImage.as_view(), name='home'),
    path('face-image/<int:pk>/', FaceImageDisplay.as_view(), name='face_image_display'),
]
