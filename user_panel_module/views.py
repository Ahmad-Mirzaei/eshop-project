from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class UserPanelDashboardPage(TemplateView):
    template_name = 'user_panel_module/user_panel_dashboard_page.html'



def user_panel_menu_component(request: HttpRequest):

    return render(request, "user_panel_module/components/user_panel_menu_component.html")