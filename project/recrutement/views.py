from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import JobAnnonce, JobMessage
from .forms import RecrutementForm, RecrutementMessageForm


@login_required
def recrutement_form(request, id=None):
    annonce = get_object_or_404(JobAnnonce, id=id) if id else None
    
    if request.method == 'POST':
        form = RecrutementForm(request.POST, instance=annonce)
        
        if form.is_valid():
            annonce = form.save()
            message = "L'annonce' a été modifiée avec succès!" if id else "L'annonce a été créée avec succès!"
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


def job_form(request, slug):
    annonce = get_object_or_404(JobAnnonce, slug=slug)

    if request.method == 'POST':
        form = RecrutementMessageForm(request.POST, request.FILES)

        if form.is_valid():
            message = form.save(commit=False)
            message.annonce = annonce
            message.save()
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

