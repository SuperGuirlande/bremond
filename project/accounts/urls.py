from django.urls import path
from django.contrib.auth import views as auth_views
from realisations.views import realisation_form, photo_form, delete_real, confirm_delete_real, photo_detail, confirm_delete_photo, delete_photo
from .views import change_password,  user_login, user_logout, admin_index
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
    path('mon-compte/', admin_index, name='admin_index'),
    path('realisation/creer/', realisation_form, name='create_realisation'),
    path('realisation/<int:id>/modifier/', realisation_form, name='edit_realisation'),
    path('realisation/<int:realisation_id>/uploader-une-photo/', photo_form, name='photo_form'),
    
    path('realisation/<int:id>/confirmer-la-suppression/', confirm_delete_real, name='confirm_delete_real'),
    path('realisation/<int:id>/supprimer/', delete_real, name='delete_real'),

    path('message/<int:id>/confirmer-la-suppression/', confirm_delete_message, name='confirm_delete_message'),
    path('message/<int:id>/supprimer/', delete_message, name='delete_message'),

    path('realisation/photo/<int:photo_id>/details/', photo_detail, name='photo_detail'),
    path('realisation/photo/<int:id>/confirmer-la-suppression/', confirm_delete_photo, name='confirm_delete_photo'),
    path('realisation/photo/<int:id>/supprimer/', delete_photo, name='delete_photo'),
]
