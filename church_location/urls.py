from django.contrib import admin
from django.urls import path
from . import  views

urlpatterns = [
    path('', views.TestMap, name = 'TestinView'),
    path('home/', views.home, name='home'),
    path('test2/',views.Testing2, name = 'testview')
]
