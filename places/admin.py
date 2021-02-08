from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin
from .models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ["preview"]

    def preview(self, obj):
        if obj.file:
            return format_html('<img src="{url}" height={height} />',
                               url=obj.file.url, height=200)
        return format_html('Здесь будет превью, когда вы выберете файл')


class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]
    search_fields = ['title']


admin.site.register(Place, PlaceAdmin)
