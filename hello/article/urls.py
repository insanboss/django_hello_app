from django.urls import path

from article.views import index_view, article_view, article_create_view

urlpatterns = [
    path('', index_view, name='article-list'),  # URL для отображения списка статей
    path('add/', article_create_view, name='article-add'),  # URL для отображения формы и создания статьи
    path('<int:pk>/', article_view, name='article-view')  # URL для просмотра деталей статьи. Обратите внимание, URL использует целочисленный параметр id
]
