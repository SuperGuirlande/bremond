import os
from django.core.exceptions import ValidationError

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Ce champ n\'accepte que les fichiers PDF.')

def validate_file_size(value):
    filesize = value.size
    
    if filesize > 10 * 1024 * 1024:  # 10MB
        raise ValidationError("La taille maximale du fichier est de 10MB")