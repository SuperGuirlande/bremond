import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from message_form.forms import ContactForm
from .models import BlogArticle, BlogCategory
from .forms import BlogArticleForm



def blog_index(request, slug=None):
    categories = BlogCategory.objects.all()

    if not slug:
        articles = BlogArticle.objects.all()
        category_selected = False
        category = None
    else:
        category_selected = True
        category = get_object_or_404(BlogCategory, slug=slug)
        articles = BlogArticle.objects.filter(categories=category)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['success'] = "Votre message nous a bien été transmis"
    else:
        form = ContactForm()

    return render(request, 'blog/index.html', context={
        'categories': categories,    
        'articles': articles,
        'category_selected': category_selected,
        'category': category,
        'form': form,
    })


@login_required
def blog_article_form(request, id=None):
    article = get_object_or_404(BlogArticle, id=id) if id else None
    
    if request.method == 'POST':
        form = BlogArticleForm(request.POST, request.FILES, instance=article)
        
        if form.is_valid():
            article = form.save()
            message = "L'article' a été modifié avec succès!" if id else "L'article a été créé avec succès!"
            request.session['success'] = message
            
            return redirect('admin_blog')
    else:
        form = BlogArticleForm(instance=article)
    
    context = {
        'form': form,
        'title': 'Modifier la réalisation' if id else 'Ajouter une réalisation',
        'article': article,
        'is_edit': id is not None,
    }
    
    return render(request, 'blog/form.html', context)


@require_http_methods(["POST"])
def create_blog_category(request):
    try:
        data = json.loads(request.body)
        title = data.get('title')
        
        if not title:
            return JsonResponse({'error': 'Le titre est requis'}, status=400)
            
        # Vérifier si la catégorie existe déjà
        if BlogCategory.objects.filter(title=title).exists():
            return JsonResponse({'error': 'Cette catégorie existe déjà'}, status=400)
            
        category = BlogCategory.objects.create(title=title)
        
        return JsonResponse({
            'id': category.id,
            'title': category.title,
            'slug': category.slug
        })
        
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Données invalides'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def article_detail(request, slug):
    article = get_object_or_404(BlogArticle, slug=slug)
    next_articles = BlogArticle.objects.all().exclude(slug=slug).order_by('-id')[:3]

    context = {
        'article': article,
        'next_articles': next_articles,
    }

    return render(request, "blog/article_detail.html", context)



@login_required
def confirm_delete_article(request, slug):
    article = get_object_or_404(BlogArticle, slug=slug)

    return render(request, "blog/confirm_delete.html", context={
        'article': article,
    })


@login_required
def delete_article(request, slug):
    article = get_object_or_404(BlogArticle, slug=slug)

    article.delete()

    return redirect('admin_blog')


