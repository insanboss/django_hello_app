from django.urls import path

from article.views import (
    IndexView,
    ArticleView,
    CreateArticleView,
    ArticleUpdateView,
    ArticleCommentCreate,
    ArticleDeleteView,
    LikeArticle,
    UnlikeArticle, LikeComment, UnlikeComment
)


app_name = 'article'

urlpatterns = [
    path('', IndexView.as_view(), name='list'),
    path('add/', CreateArticleView.as_view(), name='add'),
    path('<int:pk>/', ArticleView.as_view(), name='view'),
    path('<int:pk>/update', ArticleUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', ArticleDeleteView.as_view(), name='delete'),
    path('<int:pk>/comments/add/', ArticleCommentCreate.as_view(), name='comment-create'),
    path('<int:pk>/like_article/', LikeArticle.as_view(), name='like_article'),
    path('<int:pk>/unlike_article/', UnlikeArticle.as_view(), name='unlike_article'),
    path('<int:pk>/like_comment/', LikeComment.as_view(), name='like_comment'),
    path('<int:pk>/unlike_comment/', UnlikeComment.as_view(), name='unlike_comment'),
]
