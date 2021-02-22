from django.urls import path

from article.views import index_view, home_view, article_create_view

urlpatterns = [
    path('', index_view),
    path('add/', article_create_view)
]
