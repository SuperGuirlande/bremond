from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
import os
from uuid import uuid4


class BlogCategory(models.Model):
    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"

    title = models.CharField(verbose_name="Nom de la catégorie", max_length=255)
    slug = models.SlugField(verbose_name="Slug de l'url", max_length=100, unique=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        # Génération du slug
        if not self.slug:
            test = slugify(self.title)

            unique = test
            nb = 1

            while BlogCategory.objects.filter(slug=unique):
                unique = f"{test}-{nb}"
                nb += 1

            self.slug = unique

        super().save(*args, **kwargs)


class BlogArticle(models.Model):
    class Meta:
        verbose_name = "Article de blog"
        verbose_name_plural = "Articles de blog"

    def clean_filename(self, filename):
        """Nettoie le nom du fichier avant upload"""
        # Récupérer l'extension
        ext = filename.split('.')[-1]
        # Créer un nouveau nom à partir du titre de l'article et d'un uuid court
        clean_title = slugify(self.title)[:40]  # Limite la longueur du titre
        unique_id = str(uuid4())[:8]  # Ajoute 8 caractères uniques
        # Retourne le nouveau nom de fichier
        return f"{clean_title}-{unique_id}.{ext}"

    def thumbnail_upload_path(self, filename):
        """Définit le chemin d'upload et le nouveau nom du fichier"""
        clean_name = self.clean_filename(filename)
        return os.path.join('blog/miniatures', clean_name)

    title = models.CharField(verbose_name="Titre de l'article", max_length=255, unique=True)
    categories = models.ManyToManyField(BlogCategory, related_name="articles", verbose_name="Catégories associées")
    keywords = models.CharField(max_length=255, verbose_name="Mots clés de l'article", blank=True, null=True)
    slug = models.SlugField(verbose_name="Slug de l'article", max_length=100, unique=True)
    introduction = models.TextField(verbose_name="Introduction", blank=True, null=True)
    thumbnail = models.ImageField(
        verbose_name="Miniature de l'article",
        upload_to=thumbnail_upload_path  # Utilise notre fonction personnalisée
    )
    content = CKEditor5Field()

    created_on = models.DateField(auto_now_add=True, verbose_name="Date de création", blank=True)
    last_updated = models.DateField(auto_now_add=True, verbose_name="Date de dernière modification", blank=True)

    views = models.IntegerField(verbose_name="Nombre de vues", blank=True, default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            test = slugify(self.title)
            unique = test
            nb = 1
            while BlogArticle.objects.filter(slug=unique):
                unique = f"{test}-{nb}"
                nb += 1
            self.slug = unique
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title