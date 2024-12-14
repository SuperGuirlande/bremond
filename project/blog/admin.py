from django.contrib import admin
from .models import BlogArticle, BlogCategory


admin.site.register(BlogArticle)
admin.site.register(BlogCategory)
