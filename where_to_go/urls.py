from django.contrib import admin
from django.urls import path

from .views import show_index_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_index_page)
]
