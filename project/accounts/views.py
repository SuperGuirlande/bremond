from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from message_form.models import ContactMessage
from realisations.models import Realisation
from blog.models import BlogArticle
from recrutement.models import JobMessage


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
                return redirect('admin_index')
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
    recrutement_messages = JobMessage.objects.all().order_by('-created_on')

    context = {
        'user': user,
        'form_messages': form_messages,
        'recrutement_messages': recrutement_messages,
    }
    return render(request, 'accounts/admin_index.html', context)

@login_required
def admin_realisations(request):
    user = request.user
    realisations = Realisation.objects.all().order_by('-id')

    context = {
        'user': user,
        'realisations': realisations,
    }
    return render(request, 'accounts/admin_realisations.html', context)

@login_required
def admin_blog(request):
    user = request.user
    articles = BlogArticle.objects.all()

    context = {
        'user': user,
        'articles': articles,
    }
    return render(request, 'accounts/admin_blog.html', context)


@login_required
def admin_recrutement(request):
    from recrutement.models import JobAnnonce
    annonces = JobAnnonce.objects.all().order_by('-id')

    return render(request, "accounts/admin_recrutement.html", context={
        'annonces': annonces,
    })


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