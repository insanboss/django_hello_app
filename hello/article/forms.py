from django import forms

from article.models import Article


class ArticleForm(forms.ModelForm):
    """
    Форма для создания и редактирваония объектов статьи
    https://docs.djangoproject.com/en/3.1/ref/forms/
    """
    class Meta:
        model = Article
        fields = ('title', 'content', 'author', 'tags')


class ArticleDeleteForm(forms.Form):
    title = forms.CharField(max_length=120, required=True, label='Введите название статьи, чтобы удалить её')
