from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_, name='login'),
    path('logout/', views.logout_, name='logout'),
    path('register/', views.register, name='register'),
    path('generate/', views.generate, name='generate'),
    path('select/', views.select, name='select'),
    path('simulate/<int:pk>/', views.simulate, name='simulate'),
    path('profile/', views.profile, name='profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('faqs/', views.faqs, name='faqs')
]
