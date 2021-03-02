from django.shortcuts import render, get_object_or_404, redirect

from article.models import Article
from article.forms import ArticleForm


def index_view(request):
    """
    Представление для отображения списка статей
    """
    articles = Article.objects.all()  # Получаем список статей из базы данных
    return render(request, 'index.html', context={'articles': articles})  # Возвращаем "скомпилированный" шаблон с использованием переданного списка статей


def article_view(request, pk):  # параметр из URL передаётся в kwargs представления
    """
    Представление для отображение одной статьи
    """
    article = get_object_or_404(Article, id=pk)  # Получаем статью с помощью шотката джанго. если статья с указанным id не будет найдена - будет вывброшена ошибка 404
    return render(request, 'article_view.html', context={'article': article})


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
            article = Article.objects.create(
                title=form.cleaned_data.get('title'),
                content=form.cleaned_data.get('content'),
                author=form.cleaned_data.get('author')
            )
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
            return redirect('article-view', pk=article.id)  # после сохранения статьи перенаправим на страницу просмотра статьи

        return render(request, 'article_create.html', context={'form': form, 'article': article})  # если форма не валидна - отобразим форму с ошибками


def article_delete_view(request, pk):
    """
    Представление для удаления статьи
    """
    article = get_object_or_404(Article, id=pk)  # получаем статью

    if request.method == 'GET':  # если метод запроса GET - отобразим форму для подтверждения удаления статьи
        return render(request, 'article_delete.html', context={'article': article})
    elif request.method == 'POST':  # если метод запроса POST - удалим статью и перенаправим на страницу списка статей
        article.delete()
        return redirect('article-list')

