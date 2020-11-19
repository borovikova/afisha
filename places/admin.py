from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin
from .models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ("preview",)

    def preview(self, obj):
        return format_html('<img src="{url}" height={height} />',
                           url=obj.file.url if obj.file else None,
                           height=200
                           )


class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline,]
    search_fields = ['title']


admin.site.register(Place, PlaceAdmin)