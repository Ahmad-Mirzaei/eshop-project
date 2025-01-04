from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserPanelDashboardPage.as_view(), name='user_panel_dashboard')
]
