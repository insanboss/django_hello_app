from django.shortcuts import render, get_object_or_404, redirect

from article.models import Article


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
        return render(request, 'article_create.html')
    elif request.method == "POST":  # Если метод запроса POST - создаём статью и редиректим клиента

        # получаем данные из формы
        title = request.POST.get("title")
        content = request.POST.get("content")
        author = request.POST.get("author")

        # создаём статью
        article = Article.objects.create(
            title=title,
            content=content,
            author=author
        )

        return redirect('article-view', pk=article.id)  # Перенаправляем клиента на страницуу детального просмотра статьи
