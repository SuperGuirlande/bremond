# forms.py
from django import forms
from .models import Realisation, Category, Photo
from django_ckeditor_5.widgets import CKEditor5Widget


class RealisationForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'w-4 h-4 text-blue-600 rounded focus:ring-blue-500'
        }),
        required=True,
        label="Catégories"
    )

    class Meta:
        model = Realisation
        fields = ['title', 'content', 'categories']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full p-2 rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200',
                'placeholder': 'Titre de la réalisation'
            })
        }
        widgets = {
            "content": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="extends"
            )
        }
        labels = {
            'content': 'Contenu texte', 
        }


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'file']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full p-2 rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200',
                'placeholder': 'Titre de la photo'
            }),
            'file': forms.FileInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-md',
                'accept': 'image/*'
            })
        }
        labels = {
            'title': 'Titre de la photo',
            'file': 'Fichier image'
        }