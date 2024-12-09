from django.urls import path
from . import views

urlpatterns = [
    path('register', views.RegisterView.as_view(), name='register_page'),
    path('login', views.LoginView.as_view(), name='login_page'),
    path('activate-account/<email_active_code>', views.ActivateAccountView.as_view(), name='activate_account'),
]
