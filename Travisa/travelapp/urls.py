
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('index/', views.index, name='Home'),
    path('about/', views.about, name='About'),
    path('service/', views.service, name='Services'),
    path('contact/', views.contact, name='Contact'),

]
