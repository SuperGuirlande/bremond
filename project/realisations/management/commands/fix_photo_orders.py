from django.core.management.base import BaseCommand
from realisations.models import Realisation, Photo
from django.db import transaction

class Command(BaseCommand):
    help = 'Réinitialise les ordres des photos pour chaque réalisation'

    def handle(self, *args, **options):
        with transaction.atomic():
            for realisation in Realisation.objects.all():
                photos = Photo.objects.filter(realisation=realisation).order_by('order', 'id')
                for index, photo in enumerate(photos, 1):
                    if photo.order != index:
                        photo.order = index
                        photo.save()
                self.stdout.write(f"Réinitialisation des ordres pour la réalisation '{realisation.title}'")
        
        self.stdout.write(self.style.SUCCESS('Réinitialisation des ordres terminée avec succès')) 