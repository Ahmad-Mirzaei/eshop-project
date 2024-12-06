from django.shortcuts import render

from django.contrib.auth import get_user_model
from django.views import View
from .forms import RegisterForm
# Create your views here.


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()   # چون متد گت است دیگر لازم نیست این مدلی نوشته شود RegisterForm(request.POST or None)
        context = {
            "register_form" : register_form
        }
        return render(request, 'acount_module/register.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            # todo: register user
            pass
        context = {
            "register_form": register_form
        }
        return render(request, 'acount_module/register.html', context)


