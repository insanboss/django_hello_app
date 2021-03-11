from django.contrib import admin
from article.models import Article, Tag

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'created_at', 'updated_at']
    list_filter = ['author', 'tags']
    search_fields = ['title', 'content', 'tags']
    fields = ['id', 'title', 'author', 'tags', 'content', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at', 'id']


class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'tag', 'created_at', 'updated_at']
    list_filter = ['tag']
    search_fields = ['tag']
    fields = ['id', 'tag', 'created_at', 'updated_at']
    readonly_fields = ['id', 'created_at', 'updated_at']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)