from django.urls import path
from . import views


urlpatterns = [
    path('', views.ArticlesView.as_view(), name = "articles_page"),

]