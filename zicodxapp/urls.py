'''importing the necessary documents'''

from django.urls import path

from . import views

app_name ='zicodxapp'
urlpatterns = [
         path('', views.index, name='index'),
         ]
