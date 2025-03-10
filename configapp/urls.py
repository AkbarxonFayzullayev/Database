from django.urls import path

from configapp.views import *

urlpatterns = [
    path('index/',index),
    path('add_employee/',AddEmployee.as_view(),name='add_employee'),
    path('add_department/',AddDepartment.as_view(),name='add_department'),
    path('add_region/',AddRegion.as_view(),name='add_region'),
]
