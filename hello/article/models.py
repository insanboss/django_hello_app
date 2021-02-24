from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=120, null=False, blank=False)
    content = models.TextField(max_length=3000, null=False, blank=False)
    author = models.CharField(max_length=150, null=False, blank=False, default='Anon')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'articles'
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return f'{self.id}. {self.author}: {self.title}'
