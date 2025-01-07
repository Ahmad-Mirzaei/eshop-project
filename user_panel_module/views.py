from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
# Create your views here.


class UserPanelDashboardPage(TemplateView):
    template_name = 'user_panel_module/user_panel_dashboard_page.html'


class EditUserProfilePage(View):
    def get(self, request: HttpRequest):
        context = {}
        return render(request, "user_panel_module/edit_profile_page.html", context)

    def post(self, request: HttpRequest):
        context = {}
        return render(request, "user_panel_module/edit_profile_page.html", context)


def user_panel_menu_component(request: HttpRequest):
    return render(request, "user_panel_module/components/user_panel_menu_component.html")