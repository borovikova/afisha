from django.contrib import admin
from django.urls import path, include
from afisha import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_map),
    path('places/<int:place_id>/', views.place_detail_view, name='place-detail'),
    path('tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
