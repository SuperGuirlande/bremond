from django_ckeditor_5.widgets import CKEditor5Widget
from django import forms
from .models import BlogArticle, BlogCategory


class BlogArticleForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=BlogCategory.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'w-4 h-4 text-blue-600 rounded focus:ring-blue-500'
        }),
        required=True,
        label="Catégories"
    )

    class Meta:
        model = BlogArticle
        fields = ['title', 'categories', 'keywords', 'introduction', 'thumbnail', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full p-2 rounded-md border border-gray-300 focus:border-blue-500 focus:ring focus:ring-blue-200',
                'placeholder': "Titre de l'article"
            })
        }
        widgets = {
            "content": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5 h-[500px] rows-10"}, config_name="extends"
            )
        }
        labels = {
            'content': "Contenu de l'article", 
        }