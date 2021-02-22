from django.contrib import admin
from webapp.models import Article

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'created_at', 'updated_at']
    list_filter = ['author']
    search_fields = ['title', 'content']
    fields = ['id', 'title', 'author', 'content', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at', 'id']


admin.site.register(Article, ArticleAdmin)