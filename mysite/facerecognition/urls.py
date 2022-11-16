from django.urls import path

from . import views

app_name = 'facerecognition'

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
]