from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('login/', views.citizen_login, name='citizen_login'),
    path('register/', views.citizen_register, name='citizen_register'),
]