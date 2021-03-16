from django.urls import path

from article.views import (
    IndexView,
    ArticleView,
    article_delete_view,
    CreateArticleView,
    ArticleUpdateView
)

urlpatterns = [
    path('', IndexView.as_view(), name='article-list'),  # URL для отображения списка статей
    path('add/', CreateArticleView.as_view(), name='article-add'),  # URL для отображения формы и создания статьи
    path('<int:pk>/', ArticleView.as_view(), name='article-view'),  # URL для просмотра деталей статьи. Обратите внимание, URL использует целочисленный параметр id
    path('<int:pk>/update', ArticleUpdateView.as_view(), name='article-update'),  # URL для отображения формы и редактирования статьи
    path('<int:pk>/delete', article_delete_view, name='article-delete')  # URL для отображения формы подтверждения и удаления статьи
]
