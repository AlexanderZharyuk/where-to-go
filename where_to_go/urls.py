from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from places.views import show_index_page, get_place

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_index_page),
    path('places/<int:place_id>/', get_place),
    path('tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
