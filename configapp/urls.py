from django.urls import path

from configapp.views import  index

urlpatterns = [
    path('index/',index)
]
