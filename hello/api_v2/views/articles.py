import json

from django.http import JsonResponse
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from article.models import Article
from api_v2.serializers import ArticleSerializer


class ArticleView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            article = get_object_or_404(Article, pk=pk)
            serializer = ArticleSerializer(article)
        else:
            articles = Article.objects.all()
            serializer = ArticleSerializer(articles, many=True)
        response_data = serializer.data

        return Response(data=response_data)

    def post(self, request, *args, **kwargs):
        article_data = request.data
        serializer = ArticleSerializer(data=article_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        article_data = request.data
        serializer = ArticleSerializer(article, data=article_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        article.delete()
        return Response({'object': "deleted"})
