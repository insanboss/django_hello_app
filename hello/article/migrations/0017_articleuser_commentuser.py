# Generated by Django 3.1.6 on 2021-05-15 11:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0016_auto_20210412_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CommentUser', to='article.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CommentUser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Оценка(коммент)',
                'verbose_name_plural': 'Оценки(коммент)',
            },
        ),
        migrations.CreateModel(
            name='ArticleUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ArticleUser', to='article.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ArticleUser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Оценка(статья)',
                'verbose_name_plural': 'Оценки(статья)',
            },
        ),
    ]
