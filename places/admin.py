from adminsortable2.admin import SortableAdminMixin, SortableTabularInline
from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image


class PlaceImageInline(SortableTabularInline):
    model = Image
    extra = 0
    readonly_fields = ['preview_image']
    fields = ['image', 'preview_image']

    def preview_image(self, obj):
        return format_html(
            '<img src="{0}" style="width: auto; height:200px;" />'
            .format(obj.image.url)
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [PlaceImageInline]
    list_display = ['title']



