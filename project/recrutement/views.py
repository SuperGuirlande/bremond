from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from .models import JobAnnonce, JobMessage
from .forms import RecrutementForm, RecrutementMessageForm
from django.utils.safestring import mark_safe

@login_required
def recrutement_form(request, id=None):
    annonce = get_object_or_404(JobAnnonce, id=id) if id else None
    
    if request.method == 'POST':
        form = RecrutementForm(request.POST, instance=annonce)
        
        if form.is_valid():
            annonce = form.save()
            message = f"L'annonce '{annonce.title}' a été modifiée avec succès!" if id else "L'annonce a été créée avec succès!"
            request.session['success'] = message
            
            return redirect('admin_recrutement')
    else:
        form = RecrutementForm(instance=annonce)
    
    context = {
        'form': form,
        'title': "Modifier l'annonce" if id else "Rédiger une offre d'emploi",
        'annonce': annonce,
        'is_edit': id is not None,
    }
    
    return render(request, 'recrutement/form.html', context)


@login_required
def change_annonce_status(request, id):
    annonce = get_object_or_404(JobAnnonce, id=id)
    
    if  annonce.active:
        annonce.active = False
        message = "L'annonce à été desactivée. Elle n'est plus visible dans la page 'recrutement'"
    else:
        annonce.active = True
        message = "L'annonce à été résactivée. Elle est désormais visible dans la page 'recrutement'"

    annonce.save()

    request.session['success'] = message
    return redirect('admin_recrutement')


@login_required
def confirm_delete_annonce(request, id):
    annonce = get_object_or_404(JobAnnonce, id=id)

    return render(request, "recrutement/confirm_delete.html", context={
        'annonce': annonce,
    })



@login_required
def delete_annonce(request, id):
    annonce = get_object_or_404(JobAnnonce, id=id)
    annonce.delete()
    request.session['success'] = "L'annonce a bien été supprimée"
    return redirect('admin_recrutement')


def index(request):
    offres = JobAnnonce.objects.all().order_by('-id').exclude(active=False)

    context = {
        'offres': offres,
    }

    return render(request, "recrutement/recrutement_index.html", context)


def job_form(request, slug=None):
    if slug:
        annonce = get_object_or_404(JobAnnonce, slug=slug)
    else:
        annonce = None

    if request.method == 'POST':
        form = RecrutementMessageForm(request.POST, request.FILES)

        if form.is_valid():
            message = form.save(commit=False)
            if slug:
                message.annonce = annonce
            message.save()
            
            # Préparation du contenu HTML
            subject = f"Nouvelle candidature{' pour ' + annonce.title if annonce else ''}"
            html_content = f"""
<html>
<body>
<h2>Une nouvelle candidature a été reçue{' pour le poste : ' + annonce.title if annonce else ''}</h2>

<h3>Informations du candidat :</h3>
<ul>
    <li><strong>Nom :</strong> {message.first_name} {message.last_name}</li>
    <li><strong>Email :</strong> {message.email}</li>
    <li><strong>Téléphone :</strong> {message.phone}</li>
</ul>

<h3>Message :</h3>
{message.message}

<p>
<a href="{request.build_absolute_uri(reverse('candidature_detail', args=[message.id]))}">
    Cliquez ici pour consulter la candidature complète
</a>
</p>
</body>
</html>
            """
            
            # Création de l'email avec version texte et HTML
            text_content = strip_tags(html_content)
            email = EmailMultiAlternatives(
                subject=subject,
                body=text_content,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=['bremondrenovation@gmail.com']
            )
            email.attach_alternative(html_content, "text/html")
            email.send()
            
            request.session['success'] = "Votre message nous a bien été transmis. Nous vous enverrons une réponse dans les plus brefs délais"
            return redirect(f'{reverse("recrutement_index")}#success')
    else:
        form = RecrutementMessageForm()

    context = {
        'form': form,
        'annonce': annonce,
    }

    return render(request, 'recrutement/message.html', context)


@login_required
def confirm_delete_candidature(request, id):
    candidature = get_object_or_404(JobMessage, id=id)

    return render(request, "recrutement/confirm_delete_candidature.html", context={
        'candidature': candidature,
    })


@login_required
def delete_candidature(request, id):
    candidature = get_object_or_404(JobMessage, id=id)
    candidature.delete()
    request.session['success'] = "La candidature a bien été supprimée"
    return redirect('admin_index')


def candidature_detail(request, id):
    message = get_object_or_404(JobMessage, id=id)

    return render(request, "recrutement/candidature_detail.html", context = {
        'message': message,
    })

