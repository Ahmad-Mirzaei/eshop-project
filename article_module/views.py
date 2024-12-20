from django.shortcuts import render
from .models import Article
from django.views.generic.list import ListView
from django.views import View
# Create your views here.


# class ArticlesView(View):
#     def get(self, request):
#         articles = Article.objects.filter(is_active = True)
#         context = {'article' : articles}
#         return render(request, 'article_module/articles_page.html', context)


class ArticlesView(ListView):
    model = Article
    paginate_by = 5
    template_name = 'article_module/articles_page.html'

