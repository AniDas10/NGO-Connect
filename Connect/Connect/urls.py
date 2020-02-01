from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from NGO import views
from Event import views as event_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('show/<str:title>', views.recommend_ngo),
    path('event_rec/<str:event>', event_views.recommend_event)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
