from django.contrib.sites import requests
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views import View
from .models import User
from django.utils.crypto import get_random_string
from django.http import Http404, HttpRequest
from .forms import RegisterForm, LoginForm, ForgotPasswordForm, ResetPasswordForm
from django.contrib.auth import login, logout
from django.utils.email_service import send_email


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }

        return render(request, 'account_module/register.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'ایمیل وارد شده تکراری می باشد')
            else:
                new_user = User(
                    email=user_email,
                    email_active_code=get_random_string(72),
                    is_active=False,
                    username=user_email)
                new_user.set_password(user_password)
                new_user.save()
                # todo: send email active code
                send_email("فعال سازی حساب کاربری", new_user.email, {"user": new_user}, "emails/active_account.html")
                return redirect(reverse('login_page'))

        context = {
            'register_form': register_form
        }

        return render(request, 'account_module/register.html', context)



class ActivateAccountView(View):
    def get(self, request, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()
                # todo: show success message to user
                return redirect(reverse('login_page'))
            else:
                # todo: show your account was activated message to user
                pass

        raise Http404



class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login.html', context)

    def post(self, request: HttpRequest):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get("email")
            user_pass = login_form.cleaned_data.get("password")
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error("email", "حساب کاربری شما فعال نشده است")
                else:
                    is_password_correct = user.check_password(user_pass)
                    if is_password_correct:
                        login(request, user)
                        return redirect(reverse("home_page"))
                    else:
                        login_form.add_error("email", "کاربری با مشخصات وارد شده یافت نشد")
            else:
                login_form.add_error("email", "کاربری با مشخصات وارد شده یافت نشد")
        context = {"login_form" : login_form}
        return render(request, "account_module/login.html", context)



class ForgetPassword(View):
    def get(self, request: HttpRequest):
        forget_pass_form = ForgotPasswordForm()
        context = {"forget_pass_form" : forget_pass_form}
        return render(request, 'account_module/forgot_password.html', context)

    def post(self, request: HttpRequest):
        forget_pass_form = ForgotPasswordForm(request.POST)
        if forget_pass_form.is_valid():
            user_email = forget_pass_form.cleaned_data.get("email")
            user : User = User.objects.filter(email__iexact = user_email).first()
            if user is not None:
                # send reset password email to user
                pass
        context = {"forget_pass_form": forget_pass_form}
        return render(request, 'account_module/forgot_password.html', context)


class ResetPassword(View):
    def get(self, request: HttpRequest, active_code):
        user : User = User.objects.filter(email_active_code__iexact = active_code).first()
        if user is None:
            return redirect(reverse('login_page'))
        reset_pass_form = ResetPasswordForm()
        context = {"reset_pass_form" : reset_pass_form, "user" : user}
        return render(request, 'account_module/forgot_password.html', context)

    def post(self, request : HttpRequest, active_code):
        reset_pass_form = ResetPasswordForm(request.POST)
        user: User = User.objects.filter(email_active_code__iexact = active_code).first()
        if reset_pass_form.is_valid():
            if user is None:
                return redirect(reverse("login_page"))
            user_new_pass = reset_pass_form.cleaned_data.get("password")
            user.set_password(user_new_pass)
            user_email_active_code = get_random_string(72)
            user.is_active = True
            user.save()
            return redirect(reverse("login_page"))
        context = {"reset_pass_form": reset_pass_form, "user": user}
        return render(request, 'account_module/forgot_password.html', context)