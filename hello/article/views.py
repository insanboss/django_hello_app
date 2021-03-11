from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView, RedirectView

from article.models import Article
from article.forms import ArticleForm, ArticleDeleteForm


class IndexView(TemplateView):
    """
    Представление для просмотра списка статей. Представление реализовано с
    использованием generic-представления TemplateView.

    Поскольку метод get уже реализован в TemplateView, нам остаётся только указать
    название шаблона, который мы будем использовать в свойстве класса template_name и
    переопределить метод получения контекста get_context_data, для того, чтобы передать
    QuerySet со статьями в шаблон
    """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        kwargs['articles'] = Article.objects.all()
        return super().get_context_data(**kwargs)


class ArticleView(TemplateView):
    """
    Представление для отображения детального просмотра статьи. Как и прдставление IndexView -
    данное прдставление реализовано на основе generic - представления TemplateView.

    Переопределяем метод get_context_data для того, чтобы передать в шаблон статью и template_name,
    для того, чтобы указать какой шаблон будет отрендерен
    """
    template_name = 'article_view.html'

    def get_context_data(self, **kwargs):
        kwargs['article'] = get_object_or_404(Article, id=kwargs.get('pk'))
        return super().get_context_data(**kwargs)


def article_create_view(request):
    """
    Представление для отображения формы и создания статьи
    """
    if request.method == "GET":  # Если метод запроса GET - будет отображена форма создания статьи
        form = ArticleForm()
        return render(request, 'article_create.html', context={'form': form})
    elif request.method == "POST":  # Если метод запроса POST - создаём статью и редиректим клиента
        form = ArticleForm(data=request.POST)  # Создадим объект формы, в него передадим данные из формы, которые пришли от клиента
        if form.is_valid():  # если форма валидна - создаётся статья и клиент редиректится
            tags = form.cleaned_data.get('tags')
            article = Article.objects.create(
                title=form.cleaned_data.get('title'),
                content=form.cleaned_data.get('content'),
                author=form.cleaned_data.get('author')
            )
            article.tags.set(tags)
            return redirect('article-view', pk=article.id)  # Перенаправляем клиента на страницуу детального просмотра статьи
        return render(request, 'article_create.html', context={'form': form})  # если форма не валидна - отобразим форму с ошибками


def article_update_view(request, pk):
    """
    Представление для редактирования статьи
    """
    article = get_object_or_404(Article, id=pk)  # получаем статью

    if request.method == 'GET':  # если метод запроса GET
        form = ArticleForm(initial={  # создадим форму со стартоввыми данными полей, соответствующими данным полей статьи
            'title': article.title,
            'content': article.content,
            'author': article.author
        })
        return render(request, 'article_update.html', context={'form': form, 'article': article})  # и отобразим форму редактирования статьи
    elif request.method == 'POST':  # Если метод запроса POST
        form = ArticleForm(data=request.POST)  # Создадим объект формы, в него передадим данные из формы, которые пришли от клиента
        if form.is_valid():  # если переданные из формы данные валидны - обновим поля статьи и сохраним её
            article.title = form.cleaned_data.get("title")
            article.content = form.cleaned_data.get("content")
            article.author = form.cleaned_data.get("author")
            article.save()
            article.tags.set(form.cleaned_data.get("tags"))
            return redirect('article-view', pk=article.id)  # после сохранения статьи перенаправим на страницу просмотра статьи

        return render(request, 'article_update.html', context={'form': form, 'article': article})  # если форма не валидна - отобразим форму с ошибками


def article_delete_view(request, pk):
    """
    Представление для удаления статьи
    """
    article = get_object_or_404(Article, id=pk)  # получаем статью

    if request.method == 'GET':  # если метод запроса GET - отобразим форму для подтверждения удаления статьи
        form = ArticleDeleteForm()
        return render(request, 'article_delete.html', context={'article': article, 'form': form})
    elif request.method == 'POST':  # если метод запроса POST - удалим статью и перенаправим на страницу списка статей
        form = ArticleDeleteForm(data=request.POST)
        if form.is_valid():
            if form.cleaned_data['title'] != article.title:
                form.errors['title'] = ['Названия статей не совпадают']
                return render(request, 'article_delete.html', context={'article': article, 'form': form})

            article.delete()
            return redirect('article-list')
        return render(request, 'article_delete.html', context={'article': article, 'form': form})

