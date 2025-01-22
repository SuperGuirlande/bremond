from django.urls import path
from .views import index, services, histoire, contact, mentions, confident, google_verification
from realisations.views import realisations, realisation_detail


urlpatterns = [
    path('', index, name='index'),
    path('nos-services/', services, name='services'),
    path('notre-histoire/', histoire, name='histoire'),
    path('realisations/', realisations, name='realisations'),
    path('contact/', contact, name='contact'),
    path('realisations/categorie/<slug:category_slug>/', realisations, name='realisations_by_category'),
    path('realisations/<slug:slug>/', realisation_detail, name='realisation_detail'),
    path('mentions-legales/', mentions, name='mentions'),
    path('politique-de-confidentialite/', confident, name='confident'),
    path('google2ef000b1d95879d3.html', google_verification, name='google-verification'),
]
