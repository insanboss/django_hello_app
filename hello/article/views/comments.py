from django.views.generic import CreateView
from django.shortcuts import reverse, get_object_or_404

from article.forms import CommentForm
from article.models import Comment, Article


class ArticleCommentCreate(CreateView):
    template_name = 'comments/create.html'
    form_class = CommentForm
    model = Comment

    def get_success_url(self):
        return reverse(
            'article:view',
            kwargs={'pk': self.kwargs.get('pk')}
        )
    
    def form_valid(self, form):
        article = get_object_or_404(Article, id=self.kwargs.get('pk'))
        form.instance.article = article
        return super().form_valid(form)
