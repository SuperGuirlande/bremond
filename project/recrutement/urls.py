from django.urls import path
from .views import recrutement_form, change_annonce_status, index, job_form, candidature_detail


urlpatterns = [
    path('creer-une-annonce/', recrutement_form, name='create_annonce'),
    path('modifier-une-annonce/<int:id>/', recrutement_form, name='change_annonce'),
    path('modifier-statut-annonce/<int:id>/', change_annonce_status, name='change_annonce_status'),
    path('annonces/', index, name="recrutement_index"),
    path('<str:slug>/postuler/', job_form, name="job_form"),
    path('postuler/candidature-spontanee/', job_form, name="job_empty_form"),
    path('candidature/<int:id>/', candidature_detail, name='candidature_detail'),
]