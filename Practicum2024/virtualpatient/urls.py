from django.urls import path
from . import views

urlspatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('checkup/', views.checkup, name='checkup')
]