from django.urls import path
from .views import index, services


urlpatterns = [
    path('', index, name='index'),
    path('nos-services/', services, name='services'),
]
