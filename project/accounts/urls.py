from django.urls import path
from django.contrib.auth import views as auth_views
from realisations.views import realisation_form, photo_form, delete_real, confirm_delete_real, photo_detail, confirm_delete_photo, delete_photo
from .views import admin_blog, change_password,  user_login, user_logout, admin_index, admin_realisations, admin_recrutement
from recrutement.views import confirm_delete_annonce, delete_annonce, confirm_delete_candidature, delete_candidature
from blog.views import blog_article_form
from message_form.views import delete_message, confirm_delete_message


urlpatterns = [
    # LOGIN
    path('se-connecter/', user_login, name='login'),
    path('se-deconnecter/', user_logout, name='logout'),
    path('nouveau-mot-de-passe/', change_password, name="change_password"),

    # PASSWORD
    path('reinitialiser-mot-de-passe/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset/password_reset_form.html'), name="password_reset"),
    path('reinitialiser-mot-de-passe/envoye/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset/password_reset_done.html'), name="password_reset_done"),
    path('reinitialiser/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset/password_reset_confirm.html'), name="password_reset_confirm"),
    path('reinitialiser/termine/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset/password_reset_complete.html'), name="password_reset_complete"),

    # ADMIN
    path('administrateur/', admin_index, name='admin_index'),

    path('realisations/', admin_realisations, name='admin_realisations'),
    path('realisation/creer/', realisation_form, name='create_realisation'),
    path('realisation/<int:id>/modifier/', realisation_form, name='edit_realisation'),
    path('realisation/<int:realisation_id>/uploader-une-photo/', photo_form, name='photo_form'),
    path('realisation/<int:id>/confirmer-la-suppression/', confirm_delete_real, name='confirm_delete_real'),
    path('realisation/<int:id>/supprimer/', delete_real, name='delete_real'),

    path('blog', admin_blog, name='admin_blog'),
    path('blog/nouvel-article/', blog_article_form, name='create_article'),
    path('blog/<int:id>/modifier/', blog_article_form, name='edit_article'),

    path('recrutement/', admin_recrutement, name='admin_recrutement'),
    path('annonce/confirmer-la-suppression/<int:id>/', confirm_delete_annonce, name='confirm_delete_annonce'),
    path('annonce/supprimer/<int:id>/', delete_annonce, name='delete_annonce'),
    path('candidature/confirmer-la-suppression/<int:id>/', confirm_delete_candidature, name='confirm_delete_candidature'),
    path('candidature/supprimer/<int:id>/', delete_candidature, name='delete_candidature'),

    path('message/<int:id>/confirmer-la-suppression/', confirm_delete_message, name='confirm_delete_message'),
    path('message/<int:id>/supprimer/', delete_message, name='delete_message'),

    path('realisation/photo/<int:photo_id>/details/', photo_detail, name='photo_detail'),
    path('realisation/photo/<int:id>/confirmer-la-suppression/', confirm_delete_photo, name='confirm_delete_photo'),
    path('realisation/photo/<int:id>/supprimer/', delete_photo, name='delete_photo'),
]
