from django.urls import path
from . import views


urlpatterns = [
    path('', views.ArticlesView.as_view(), name = "articles_page"),
    path('cat/<str:category>', views.ArticlesView.as_view(), name = "articles_by_category_page"),

]