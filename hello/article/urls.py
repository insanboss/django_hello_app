from django.urls import path

from article.views import index_view, article_view, article_create_view

urlpatterns = [
    path('', index_view),  # URL для отображения списка статей
    path('articles/add/', article_create_view),  # URL для создания статьи
    path('article/', article_view)  # URL для просмотра деталей статьи
]
