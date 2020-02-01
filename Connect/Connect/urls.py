from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from NGO import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('show/<str:title>', views.recommend_ngo)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
