from django.core import paginator
from django.shortcuts import render
from .models import Article, ArticleCategory, ArticlesComment
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views import View
from django.http import HttpRequest, HttpResponse


# Create your views here.


class ArticlesView(ListView):
    model = Article
    paginate_by = 4
    template_name = 'article_module/articles_page.html'

    def get_context_data(self,*args, **kwargs):
        context = super(ArticlesView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        query = super(ArticlesView, self).get_queryset()
        query = query.filter(is_active = True)
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(selected_categories__url_title__iexact = category_name)
        return query


def article_categories_component(request: HttpRequest):
    article_main_categories = ArticleCategory.objects.filter(is_active = True, parent_id = None)
    context = {'main_categories' : article_main_categories}
    return render(request, 'article_module/components/article_categories_component.html', context)



class ArticlesDetailView(DetailView):
    model = Article
    template_name = 'article_module/article_detail_page.html'

    def get_queryset(self):
        query = super(ArticlesDetailView, self).get_queryset()
        query = query.filter(is_active = True)
        return query

    def get_context_data(self, **kwargs):
        context = super(ArticlesDetailView, self).get_context_data()
        article : Article = kwargs.get('object')
        context['comments'] = ArticlesComment.objects.filter(article_id=article.id, parent=None).prefetch_related('articlescomment_set')
        return context


def add_article_comment(request: HttpRequest):
    print(request.GET)
    return HttpResponse("response")