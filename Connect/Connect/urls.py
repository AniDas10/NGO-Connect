from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from NGO import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('populate_once/', views.populate_once),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
