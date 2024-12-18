from django.shortcuts import render
from django.views.generic.base import TemplateView
from site_module.models import SiteSetting
# Create your views here.



class HomeView(TemplateView):
    template_name = 'home_module/index_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = 'this is data in home page'
        context['message'] = 'this is message in home page'
        return context


def site_header_component(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting = True).first()
    context = {"site_setting" : setting}
    return render(request, 'shared/site_header_component.html', context)


def site_footer_component(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting = True).first()
    context = {"site_setting" : setting}
    return render(request, 'shared/site_footer_component.html', context)
