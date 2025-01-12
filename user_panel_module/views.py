from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from .forms import EditProfileModelForm
from account_module.models import User

class UserPanelDashboardPage(TemplateView):
    template_name = 'user_panel_module/user_panel_dashboard_page.html'


class EditUserProfilePage(View):
    def get(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form = EditProfileModelForm(instance= current_user)
        context = {
            'form': edit_form,
            'current_user' : current_user
        }
        return render(request, 'user_panel_module/edit_profile_page.html', context)

    def post(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form = EditProfileModelForm(request.POST, request.FILES, instance=current_user)
        if edit_form.is_valid():
            edit_form.save(commit=True)
        context = {
            'form' : edit_form,
            'current_user': current_user
        }
        return render(request, 'user_panel_module/edit_profile_page.html', context)


class ChangePasswordPage(View):
    def get(self, request: HttpRequest):
        return render(request, 'user_panel_module/change_password_page.html')

    def post(self, request: HttpRequest):

        pass


def user_panel_menu_component(request: HttpRequest):
    return render(request, 'user_panel_module/components/user_panel_menu_component.html')
