from django.shortcuts import redirect, render
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.utils.timezone import localtime
from message_form.forms import ContactForm
from django.http import HttpResponse


def send_contact_email(message, request=None):
    date = localtime(message.created_on).strftime("%d/%m/%Y à %H:%M")
    subject = "Nouveau message de contact"
    html_content = f"""
<html>
<body>
<h2>Un nouveau message a été reçu via le formulaire de contact</h2>

<h3>Informations du contact :</h3>
<ul>
    <li><strong>Prénom :</strong> {message.first_name}</li>
    <li><strong>Nom :</strong> {message.last_name}</li>
    <li><strong>Email :</strong> {message.email}</li>
    <li><strong>Téléphone :</strong> {message.phone}</li>
    <li><strong>Reçu le :</strong> {date}</li>
</ul>

<h3>Message :</h3>
{message.message}

</body>
</html>
    """
    
    email = EmailMultiAlternatives(
        subject=subject,
        body=html_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        # to=['contact@agencecodemaster.com']
        to=['bremondrenovation@gmail.com']
    )
    email.attach_alternative(html_content, "text/html")
    email.send()


def index(request):
    user = request.user

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.save()
            send_contact_email(message, request)
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
            message = form.save()
            send_contact_email(message, request)
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
            message = form.save()
            send_contact_email(message, request)
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
            message = form.save()
            send_contact_email(message, request)
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


def google_verification(request):
    verification_content = "google-site-verification: google2ef000b1d95879d3.html"
    return HttpResponse(verification_content, content_type="text/plain")

