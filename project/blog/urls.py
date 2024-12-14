from django.urls import path
from .views import blog_index, article_detail, confirm_delete_article, delete_article

urlpatterns = [
    path('', blog_index, name="blog_index"),
    path('<str:slug>/', blog_index, name="blog_category"),
    path('article/<str:slug>/', article_detail, name='article_detail'),
    path('article/confirmer-suppression/<str:slug>/', confirm_delete_article, name='confirm_delete_article'),
    path('article/supprimer/<str:slug>/', delete_article, name='delete_article'),
]