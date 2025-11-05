from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.destination, name='destination'),
    path('destinations/<slug:slug>/', views.destination_detail, name='destination_detail'),
    
] 
