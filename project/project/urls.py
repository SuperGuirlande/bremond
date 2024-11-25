from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from realisations.views import create_category


urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('compte/', include('accounts.urls')),

    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('api/categories/create/', create_category, name='api_create_category'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)