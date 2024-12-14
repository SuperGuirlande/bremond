import json
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.db.models import Count
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Realisation, Category, Photo
from .forms import RealisationForm, PhotoForm
from message_form.forms import ContactForm


def realisations(request, category_slug=None):
    categories_with_reals = Category.objects.annotate(
        real_count=Count('realisations')
    ).filter(real_count__gt=0)
    
    realisations = Realisation.objects.all().order_by('-created_on')
    
    selected_category = None
    if category_slug:
        selected_category = get_object_or_404(Category, slug=category_slug)
        realisations = realisations.filter(categories=selected_category)

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
        'categories': categories_with_reals,
        'realisations': realisations,
        'selected_category': selected_category,
        'form': form,
    }
    
    return render(request, 'main/realisations.html', context)


def realisation_detail(request, slug):
    realisation = get_object_or_404(Realisation, slug=slug)
    photos = realisation.photos.all()  # Récupère toutes les photos associées
    
    context = {
        'realisation': realisation,
        'photos': photos,
    }
    
    return render(request, 'realisations/realisation_detail.html', context)


@require_http_methods(["POST"])
def create_category(request):
    try:
        data = json.loads(request.body)
        title = data.get('title')
        
        if not title:
            return JsonResponse({'error': 'Le titre est requis'}, status=400)
            
        # Vérifier si la catégorie existe déjà
        if Category.objects.filter(title=title).exists():
            return JsonResponse({'error': 'Cette catégorie existe déjà'}, status=400)
            
        category = Category.objects.create(title=title)
        
        return JsonResponse({
            'id': category.id,
            'title': category.title,
            'slug': category.slug
        })
        
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Données invalides'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    

def realisation_form(request, id=None):
    realisation = get_object_or_404(Realisation, id=id) if id else None
    
    if request.method == 'POST':
        form = RealisationForm(request.POST, instance=realisation)
        
        if form.is_valid():
            realisation = form.save()
            message = "La réalisation a été modifiée avec succès!" if id else "La réalisation a été créée avec succès!"
            request.session['success'] = message
            
            return redirect('admin_realisations')
    else:
        form = RealisationForm(instance=realisation)
    
    context = {
        'form': form,
        'title': 'Modifier la réalisation' if id else 'Ajouter une réalisation',
        'realisation': realisation,
        'is_edit': id is not None,
    }
    
    return render(request, 'realisations/form.html', context)


def photo_form(request, realisation_id):
    realisation = get_object_or_404(Realisation, id=realisation_id)

    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            new_photo = form.save(commit=False)
            new_photo.realisation = realisation
            new_photo.save()
            base_url = reverse_lazy('admin_index')
            return HttpResponseRedirect(f'{base_url}#realisation_{realisation.id}')
        else:
            print(form.errors)
    else:
        form = PhotoForm()

    context = {
        'form': form,
        'realisation': realisation,
    }

    return render(request, 'realisations/photo_form.html', context)


def photo_detail(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)

    context = {
        'photo': photo,
    }

    return render(request, 'realisations/photo_detail.html', context)



def confirm_delete_real(request, id):
    real = get_object_or_404(Realisation, id=id)

    context = {
        'real': real,
    }

    return render(request, "realisations/confirm_delete_real.html", context)


def delete_real(request, id):
    real = get_object_or_404(Realisation, id=id)
    title = real.title
    real.delete()

    request.session['success'] = f"La réatisation {title} à bien été supprimée"
    return redirect('admin_index')



def confirm_delete_photo(request, id):
    photo = get_object_or_404(Photo, id=id)

    context = {
        'photo': photo,
    }

    return render(request, "realisations/confirm_delete_photo.html", context)


def delete_photo(request, id):
    photo = get_object_or_404(Photo, id=id)
    title = photo.title
    photo.delete()

    request.session['success'] = f"La photo {title} à bien été supprimée"
    return redirect('admin_index')
