from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.text import slugify
 
 
class Category(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Nom de la catégorie")
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):

        if not self.slug:
            test = slugify(self.title)
            unique = test
            nb = 1
            while Category.objects.filter(slug=unique):
                unique = f"{test}-{nb}"
                nb += 1
            self.slug = unique
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Realisation(models.Model):
    title = models.CharField(verbose_name="Titre", max_length=255, unique=True)
    slug = models.SlugField(verbose_name="Slug" , max_length=120, blank=True, null=True, unique=True)
    content = CKEditor5Field('content', config_name='extends')

    categories = models.ManyToManyField(Category, related_name="realisations", verbose_name="Catégories associées")

    created_on = models.DateField(auto_now_add=True, verbose_name="Date de création", blank=True)
    last_updated = models.DateField(auto_now_add=True, verbose_name="Date de dernière modification", blank=True)


    def save(self, *args, **kwargs):
        # Génération d'un slug unique
        if not self.slug:
            test = slugify(self.title)

            unique = test
            nb = 1

            while Realisation.objects.filter(slug=unique).exists():
                unique = f"{test}-{nb}"
                nb += 1
            
            self.slug = unique
        
        super().save(*args, **kwargs)


class Photo(models.Model):
    title = models.CharField(max_length=255, verbose_name="Titre de la photo")
    file = models.ImageField(verbose_name="Fichier image", upload_to="realisations/photo")
    realisation = models.ForeignKey(Realisation, on_delete=models.CASCADE, related_name='photos', blank=True)
    order = models.IntegerField(default=1, verbose_name="Ordre d'affichage")
    is_thumbnail = models.BooleanField(default=False, verbose_name="Est une image de couverture")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):    
        if self._state.adding:  # Si c'est une nouvelle photo
            max_order = Photo.objects.filter(realisation=self.realisation).aggregate(models.Max('order'))['order__max']
            self.order = (max_order or 0) + 1
        super().save(*args, **kwargs)

    def move_up(self):
        from django.db import transaction
        
        with transaction.atomic():
            # Récupérer toutes les photos de la réalisation, triées par ordre
            photos = list(Photo.objects.filter(realisation=self.realisation).order_by('order'))
            
            # Trouver l'index actuel
            current_index = next((i for i, p in enumerate(photos) if p.id == self.id), -1)
            
            if current_index > 0:  # Si ce n'est pas la première photo
                # Échanger avec la photo précédente
                photos[current_index], photos[current_index - 1] = photos[current_index - 1], photos[current_index]
                
                # Mettre à jour les ordres
                for i, photo in enumerate(photos, 1):
                    if photo.order != i:
                        photo.order = i
                        photo.save()

    def move_down(self):
        from django.db import transaction
        
        with transaction.atomic():
            # Récupérer toutes les photos de la réalisation, triées par ordre
            photos = list(Photo.objects.filter(realisation=self.realisation).order_by('order'))
            
            # Trouver l'index actuel
            current_index = next((i for i, p in enumerate(photos) if p.id == self.id), -1)
            
            if current_index < len(photos) - 1:  # Si ce n'est pas la dernière photo
                # Échanger avec la photo suivante
                photos[current_index], photos[current_index + 1] = photos[current_index + 1], photos[current_index]
                
                # Mettre à jour les ordres
                for i, photo in enumerate(photos, 1):
                    if photo.order != i:
                        photo.order = i
                        photo.save()


