from django.shortcuts import render
from .models import Article, ArticleCategory
from django.views.generic.list import ListView
from django.views import View
from jalali_date import datetime2jalali, date2jalali
import datetime
from django.http import HttpRequest
# Create your views here.


# class ArticlesView(View):
#     def get(self, request):
#         articles = Article.objects.filter(is_active = True)
#         context = {'article' : articles}
#         return render(request, 'article_module/articles_page.html', context)


class ArticlesView(ListView):
    model = Article
    paginate_by = 10
    template_name = 'article_module/articles_page.html'

    def get_context_data(self,*args, **kwargs):
        context = super(ArticlesView, self).get_context_data(*args, **kwargs)
        return context


def article_categories_component(request: HttpRequest):
    article_main_categories = ArticleCategory.objects.filter(is_active = True, parent_id = None)
    context = {'main_categories' : article_main_categories}
    return render(request, 'article_module/components/article_categories_component.html', context)
