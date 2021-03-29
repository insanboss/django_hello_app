from django.urls import path

from article.views import (
    IndexView,
    ArticleView,
    CreateArticleView,
    ArticleUpdateView,
    ArticleCommentCreate,
    ArticleDeleteView
)

urlpatterns = [
    path('', IndexView.as_view(), name='article-list'),
    path('add/', CreateArticleView.as_view(), name='article-add'),
    path('<int:pk>/', ArticleView.as_view(), name='article-view'),
    path('<int:pk>/update', ArticleUpdateView.as_view(), name='article-update'),
    path('<int:pk>/delete', ArticleDeleteView.as_view(), name='article-delete'),
    path('<int:pk>/comments/add/', ArticleCommentCreate.as_view(), name='article-commnet-create')
]
