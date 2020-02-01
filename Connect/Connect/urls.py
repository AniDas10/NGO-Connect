from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ngo/', include('NGO.urls')),
    path('event/', include('Event.urls')),
    path('citizen/', include('Citizen.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
