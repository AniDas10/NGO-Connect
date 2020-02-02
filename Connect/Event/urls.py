from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('recommend/<str:event>/', views.recommend_event, name='recommend_event'),
    path('volunteer/<int:id>', views.volunteer_event, name='volunteer_event'),
]