from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.text import slugify
from .validators import validate_file_extension, validate_file_size


class JobAnnonce(models.Model):
    class Meta:
        verbose_name = "Offre d'emploi"
        verbose_name_plural = "Offres d'emploi"


    title = models.CharField(verbose_name="Titre de l'annonce", max_length=255)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    content = CKEditor5Field()
    active = models.BooleanField(verbose_name="Statut", default=True)

    job = models.CharField(max_length=255, verbose_name="Intitulé du poste")
    contract_type = models.CharField(max_length=50, verbose_name="Type de contrat")
    experience = models.IntegerField(verbose_name="Expérience exigée (en année)", null=True, blank=True)
    contract_length = models.IntegerField(verbose_name="Durée du contrat (en mois)", blank=True, null=True)

    hebdo = models.IntegerField(verbose_name="Temps de travail", blank=True, null=True)
    salaire = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Rémunération brute", blank=True, null=True)

    created_on = models.DateField(auto_now_add=True, verbose_name="Date de création", blank=True)
    last_updated = models.DateField(auto_now=True, verbose_name="Dernière modifications", blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # Génération d'un slug unique
        if not self.slug:
            test = slugify(self.title)
            unique = test
            nb = 1

            while JobAnnonce.objects.filter(slug=unique).exists():
                unique = f"{test}-{nb}"
                nb += 1

            self.slug = unique

        # Sauvegarde
        super().save(*args, **kwargs)


class JobMessage(models.Model):
    class Meta:
        verbose_name="Formulaire de recrutement"
        verbose_name_plural="Formulaires de recrutement"

    annonce = models.ForeignKey(JobAnnonce, verbose_name="Annonce associée", on_delete=models.SET_NULL, related_name="messages", blank=True, null=True)

    first_name = models.CharField(verbose_name="Prenom", max_length=255)
    last_name = models.CharField(verbose_name="Nom", max_length=255)
    email = models.EmailField(verbose_name="Adresse email")
    phone = models.CharField(verbose_name="N° de téléphone", max_length=16)

    message = CKEditor5Field()

    cv = models.FileField(
        upload_to='recrutement/cv', 
        verbose_name='CV',
        validators=[validate_file_extension, validate_file_size],
        help_text="Format accepté : PDF uniquement. Taille max : 10MB"
    )
    lm = models.FileField(
        upload_to='recrutement/lm', 
        verbose_name="Lettre de motivation",
        validators=[validate_file_extension, validate_file_size],
        help_text="Format accepté : PDF uniquement. Taille max : 10MB"
    )

    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Date de reception")

    def __str__(self):
        return f"Reçu le {self.created_on} | {self.first_name} {self.last_name} | Pour le poste de {self.annonce.job}"
    


