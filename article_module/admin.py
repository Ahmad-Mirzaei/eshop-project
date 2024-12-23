from django.contrib import admin
from . import models
from django.http import HttpRequest

from .models import Article


# Register your models here.

@admin.register(models.ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_title', 'parent', 'is_active']
    list_editable = ['url_title', 'parent', 'is_active']


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'short_description', 'is_active']
    list_editable = ['is_active',]

    def save_model(self, request: HttpRequest, obj: Article, form, change):
        if not change:
                obj.author = request.user
        return super().save_model(request, obj, form, change)


@admin.register(models.ArticlesComment)
class ArticlesCommentAdmin(admin.ModelAdmin):
    list_display = ['article', 'parent', 'user', 'create_date']