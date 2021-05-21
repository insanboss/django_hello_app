"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings


HOMEPAGE_URL = 'articles/'  # константа для хранения домашней страницы. на данную страницу будет произведён редирект, когда пользователь зайдёт по пути /


urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('article.urls')),  # подключаем URLs из приложения article
    path('accounts/', include('accounts.urls')),
    path('', RedirectView.as_view(url=HOMEPAGE_URL, permanent=True)),  # перенаправляем на страницу просмотра списка статей
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
