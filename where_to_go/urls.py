from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import show_index_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_index_page)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
