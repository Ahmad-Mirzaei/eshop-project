from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, 'home_module/index_page.html')

# class HomeView(TemplateView):
#     template_name = 'home_module/index_page.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['data'] = "this is message in home page"
#         return context


def site_header_component(request):
    context = {
        'link': 'آموزش جنگو'
    }
    return render(request, 'shared/site_header_component.html', context)


def site_footer_component(request):
    return render(request, 'shared/site_footer_component.html', {})
