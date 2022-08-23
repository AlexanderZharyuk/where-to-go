from django.contrib import admin

from .models import Place, Image


class PlaceImageInline(admin.TabularInline):
    model = Image
    extra = 0


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlaceImageInline]
