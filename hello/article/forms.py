from django import forms
from django.forms import widgets


class ArticleForm(forms.Form):
    """
    Форма для создания и редактирваония объектов статьи
    https://docs.djangoproject.com/en/3.1/ref/forms/
    """
    title = forms.CharField(max_length=120, required=True, label='Заголовок')
    content = forms.CharField(max_length=3000, required=True, widget=widgets.Textarea, label='Контент')
    author = forms.CharField(max_length=150, required=True, label='Автор')
