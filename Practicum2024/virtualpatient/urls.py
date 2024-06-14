from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('generate/', views.generate, name='generate'),
    path('select/', views.select, name='select'),
    path('simulate/', views.simulate, name='simulate'),
    path('profile/', views.profile, name='profile'),
    path('faqs/', views.faqs, name='faqs')
]