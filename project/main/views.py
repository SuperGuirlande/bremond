from django.shortcuts import redirect, render
from message_form.forms import ContactForm


def index(request):
    user = request.user

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['success'] = "Votre message à été envoyé. Vous serez contacté prochainement"
        else:
            request.session['alert'] = "Il y a un problème avec les informations fournies"
    else:
        form = ContactForm()

    context = {
        'user': user,
        'form': form,
    }
    return render(request, 'main/index.html', context)


def services(request):
    user = request.user

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['success'] = "Votre message à été envoyé. Vous serez contacté prochainement"
        else:
            request.session['alert'] = "Il y a un problème avec les informations fournies"
    else:
        form = ContactForm()

    context = {
        'user': user,
        'form': form,
    }
    return render(request, 'main/services.html', context)


def histoire(request):
    user = request.user

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['success'] = "Votre message à été envoyé. Vous serez contacté prochainement"
        else:
            request.session['alert'] = "Il y a un problème avec les informations fournies"
    else:
        form = ContactForm()

    context = {
        'user': user,
        'form': form,
    }
    return render(request, 'main/histoire.html', context)


def contact(request):
    user = request.user

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            request.session['success'] = "Votre message nous a bien été envoyé ! Vous serez contacté(e) dans les plus brefs délais."
    else:
        form = ContactForm()

    context = {
        'form': form,
        'user': user,
    }

    return render(request, "main/contact.html", context)


def mentions(request):
    return render(request, 'main/mentions.html')

def confident(request):
    return render(request, 'main/confident.html')

