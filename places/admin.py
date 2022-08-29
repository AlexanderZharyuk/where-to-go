from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase
from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image


class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 0
    readonly_fields = ['preview_image']
    fields = ['image', 'preview_image']

    def preview_image(self, obj, max_height='200px'):
        return format_html(
            '<img src="{url}" height="{max_height}" />',
            url=obj.image.url,
            max_height=max_height
        )
    preview_image.short_description = 'Превью'


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [PlaceImageInline]
