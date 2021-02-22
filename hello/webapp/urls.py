from django.urls import path

from webapp.views import index_view, home_view, article_create_view

urlpatterns = [
    path('hello/', index_view),
    path('', home_view),
    path('add/', article_create_view)
]
