from django import forms
from .models import ContactMessage
from django.core.validators import RegexValidator


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['last_name', 'first_name', 'email', 'phone', 'message']

    phone_regex = RegexValidator(
            regex=r'^(0[67](\s?\d{2}){4})$',
            message="Le numéro de téléphone doit être au format '06 06 06 06 06' ou '0606060606'."
        )
    phone = forms.CharField(label='Numéro de téléphone', validators=[phone_regex], max_length=14)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['last_name'].widget.attrs['placeholder'] = "Votre nom"
        self.fields['first_name'].widget.attrs['placeholder'] = "Votre prénom"
        self.fields['email'].widget.attrs['placeholder'] = "exemple@email.com"
        self.fields['phone'].widget.attrs['placeholder'] = "06 07 08 09 10"
        self.fields['message'].widget.attrs['placeholder'] = "Laissez nous votre message. Nous prendrons contact avec vous dans les plus brefs delais"