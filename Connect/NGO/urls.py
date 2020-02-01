from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('<str:title>/', views.recommend_ngo, name='recommend_ngo'),
    path('follow/<int:id>', views.follow_ngo, name='follow_ngo')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
