from django import forms
from django.contrib.auth.forms import  AuthenticationForm
from django.utils.translation import gettext_lazy as _


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label=_("Adresse e-mail"), widget=forms.TextInput)
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput)


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput())
    new_password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

