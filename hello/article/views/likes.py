from django.contrib.auth import get_user_model
from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.views import View

from article.models import Article, ArticleUser, Comment, CommentUser


class LikeArticle(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=self.kwargs.get('pk'))
        user = request.user
        try:
            ArticleUser.objects.get(article=article, user=user)
            return HttpResponseForbidden('you already liked that')
        except ArticleUser.DoesNotExist:
            ArticleUser.objects.create(article=article, user=user)
            return HttpResponse(article.ArticleUser.count())


class UnlikeArticle(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=self.kwargs.get('pk'))
        user = request.user
        try:
            like = ArticleUser.objects.get(article=article, user=user)
            like.delete()
            return HttpResponse(article.ArticleUser.count())
        except ArticleUser.DoesNotExist:
            return HttpResponseForbidden('you already unliked that')


class LikeComment(View):
    def get(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=self.kwargs.get('pk'))
        user = request.user
        try:
            CommentUser.objects.get(comment=comment, user=user)
            return HttpResponseForbidden('you already liked that')
        except CommentUser.DoesNotExist:
            CommentUser.objects.create(comment=comment, user=user)
            return HttpResponse(comment.CommentUser.count())


class UnlikeComment(View):
    def get(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=self.kwargs.get('pk'))
        user = request.user
        try:
            like = CommentUser.objects.get(comment=comment, user=user)
            like.delete()
            return HttpResponse(comment.CommentUser.count())
        except CommentUser.DoesNotExist:
            return HttpResponseForbidden('You already unliked that')


