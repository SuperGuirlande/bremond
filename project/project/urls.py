from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from realisations.views import create_category
from blog.views import create_blog_category


urlpatterns = [
    path('', include('main.urls')),
    path('blog/', include('blog.urls')),
    path('recrutement/', include('recrutement.urls')),
    path('admin/', admin.site.urls),
    path('compte/', include('accounts.urls')),

    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('api/categories/create/', create_category, name='api_create_category'),
    path('api/blog-categories/create/', create_blog_category, name='api_create_blog_category'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)