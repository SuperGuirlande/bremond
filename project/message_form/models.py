from django.db import models    
from django.utils.timezone import localtime


class ContactMessage(models.Model):
    first_name = models.CharField(max_length=255, verbose_name="Prénom")
    last_name = models.CharField(max_length=255, verbose_name="Nom")
    email = models.EmailField(verbose_name="Adresse email")
    phone = models.CharField(max_length=16, verbose_name="N° de téléphone")
    message = models.TextField(verbose_name="Message")

    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Message reçu le", null=True)

    def __str__(self):
        date = localtime(self.created_on).strftime("%d/%m/%Y à %H:%M")
        return f"{self.first_name} {self.last_name} | Réçu le : {date} | {self.phone} | {self.email}"

