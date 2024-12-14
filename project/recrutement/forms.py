from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import JobAnnonce, JobMessage

class RecrutementMessageForm(forms.ModelForm):
    class Meta:
        model = JobMessage
        fields = ['first_name', 'last_name', 'email', 'phone', 'message', 'cv', 'lm']
        widgets = {
            "message": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="default"
            )
        }
            

class RecrutementForm(forms.ModelForm):
    class Meta:
        model = JobAnnonce
        fields = ['title', 'content', 'job', 'contract_type', 'experience', 'contract_length', 'hebdo', 'salaire']
        widgets = {
            "title": forms.TextInput(
                attrs={"placeholder": "Ex: Recherche couvreur pendant 3 mois à Jonzac"}
            ),
            "job": forms.TextInput(
                attrs={"placeholder": "Ex: Couvreur Zingueur / Charpentier"}
            ),
            "experience": forms.NumberInput(
                attrs={"placeholder": "Facultatif"}
            ),
            "contract_type": forms.TextInput(
                attrs={"placeholder": "Ex: CDD / CDI"}
            ),
            "contract_length": forms.NumberInput(
                attrs={"placeholder": "Facultatif"}
            ),
            "salaire": forms.NumberInput(
                attrs={"placeholder": "Facultatif"}
            ),
            "hebdo": forms.NumberInput(
                attrs={"placeholder": "Facultatif"}
            ),
            "content": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="extends"
            )
        }
        
