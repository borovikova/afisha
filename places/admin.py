from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ("preview",)

    def preview(self, obj):
        return format_html('<img src="{url}" height={height} />',
                           url=obj.file.url,
                           # width=obj.headshot.width,
                           height=200
                           )


class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(Image)
admin.site.register(Place, PlaceAdmin)
