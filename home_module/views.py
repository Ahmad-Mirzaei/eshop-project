from django.shortcuts import render
from django.views.generic.base import TemplateView
from site_module.models import SiteSetting, FooterLinkBox, Slider

# Create your views here.



class HomeView(TemplateView):
    template_name = 'home_module/index_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slider = Slider.objects.filter(is_active = True)
        context["sliders"] = slider
        return context


def site_header_component(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting = True).first()
    context = {"site_setting" : setting}
    return render(request, 'shared/site_header_component.html', context)


def site_footer_component(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting = True).first()
    footer_link_boxes = FooterLinkBox.objects.all()
    for item in footer_link_boxes:
        item.footerlink_set

    context = {"site_setting" : setting, "footer_link_boxes" : footer_link_boxes}
    return render(request, 'shared/site_footer_component.html', context)


class AboutView(TemplateView):
    template_name = 'home_module/about_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        site_setting: SiteSetting = SiteSetting.objects.filter(is_main_setting = True).first()
        context["site_setting"] = site_setting
        return context