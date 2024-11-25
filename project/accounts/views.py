from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from message_form.models import ContactMessage
from realisations.models import Realisation


### ACCOUNT ###
# Login
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                print("Authentication failed: user is None")
        else:
            print("Form is not valid")
    else:
        form = UserLoginForm()

    return render(request, 'accounts/login.html', {'form': form})

# Logout
@login_required
def user_logout(request):
    logout(request)
    return redirect('index')


### ESPACE ADMINISTRATEUR ###

# Index Admin
@login_required
def admin_index(request):
    user = request.user
    form_messages = ContactMessage.objects.all().order_by('-created_on')
    realisations = Realisation.objects.all().order_by('-id')

    context = {
        'user': user,
        'form_messages': form_messages,
        'realisations': realisations,
    }
    return render(request, 'accounts/admin_index.html', context)




### MOT DE PASSE ###
# Change password
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) 
            messages.success(request, 'Votre mot de passe a été changé avec succès.')
            return redirect(reverse_lazy('my_account'))
        else:
            messages.error(request, 'Veuillez corriger les erreurs ci-dessous.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/password_reset/change_password.html', {'form': form})