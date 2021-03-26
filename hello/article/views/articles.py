from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import FormView, ListView, CreateView, DetailView
from django.urls import reverse
from django.db.models import Q
from django.utils.http import urlencode

from article.models import Article
from article.forms import ArticleForm, ArticleDeleteForm, SearchForm


class IndexView(ListView):
    """
    Представление для просмотра списка статей. Представление реализовано с
    использованием generic-представления ListView.

    В представлении активирована пагинация и реализован поиск
    """
    template_name = 'articles/index.html'
    model = Article
    context_object_name = 'articles'
    ordering = ('title', '-created_at')
    paginate_by = 5
    paginate_orphans = 1

    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()
        return super(IndexView, self).get(request, **kwargs)
    
    def get_queryset(self):
        queryset = super().get_queryset()

        if self.search_data:
            queryset = queryset.filter(
                Q(title__icontains=self.search_data) |
                Q(author__icontains=self.search_data) |
                Q(content__icontains=self.search_data)
            )
        return queryset

    def get_search_data(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search_value']
        return None
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form

        if self.search_data:
            context['query'] = urlencode({'search_value': self.search_data})

        return context


class ArticleView(DetailView):
    model = Article
    template_name = 'articles/view.html'


class CreateArticleView(CreateView):
    template_name = 'articles/create.html'
    form_class = ArticleForm
    model = Article

    def form_valid(self, form):
        tags = form.cleaned_data.pop('tags')
        article = Article()
        for key, value in form.cleaned_data.items():
            setattr(article, key, value)

        article.save()
        article.tags.set(tags)

        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('article-list')


class ArticleUpdateView(FormView):
    form_class = ArticleForm
    template_name = 'articles/update.html'

    def dispatch(self, request, *args, **kwargs):
        self.article = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        return super().get_initial()

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.article
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = self.article
        return context

    def get_object(self):
        article = get_object_or_404(
            Article, id=self.kwargs.get('pk')
            )
        return article

    def form_valid(self, form):
        tags = form.cleaned_data.pop('tags')
        form.save()
        self.article.tags.set(tags)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('article-view', kwargs={'pk': self.kwargs.get('pk')})


def article_delete_view(request, pk):
    """
    Представление для удаления статьи
    """
    article = get_object_or_404(Article, id=pk)  # получаем статью

    if request.method == 'GET':  # если метод запроса GET - отобразим форму для подтверждения удаления статьи
        form = ArticleDeleteForm()
        return render(request, 'articles/delete.html', context={'article': article, 'form': form})
    elif request.method == 'POST':  # если метод запроса POST - удалим статью и перенаправим на страницу списка статей
        form = ArticleDeleteForm(data=request.POST)
        if form.is_valid():
            if form.cleaned_data['title'] != article.title:
                form.errors['title'] = ['Названия статей не совпадают']
                return render(request, 'articles/delete.html', context={'article': article, 'form': form})

            article.delete()
            return redirect('article-list')
        return render(request, 'articles/delete.html', context={'article': article, 'form': form})
