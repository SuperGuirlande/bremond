from django.urls import path
from .views import index, services, histoire
from realisations.views import realisations, realisation_detail


urlpatterns = [
    path('', index, name='index'),
    path('nos-services/', services, name='services'),
    path('notre-histoire/', histoire, name='histoire'),
    path('realisations/', realisations, name='realisations'),
    path('realisations/categorie/<slug:category_slug>/', realisations, name='realisations_by_category'),
    path('realisations/<slug:slug>/', realisation_detail, name='realisation_detail'),
]
