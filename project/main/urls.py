from django.urls import path
from .views import index, services, histoire


urlpatterns = [
    path('', index, name='index'),
    path('nos-services/', services, name='services'),
    path('notre-histoire/', histoire, name='histoire'),
]
