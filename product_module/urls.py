from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name = "product-list"),
    path(route = '<int:pk>/', view = views.product_detail, name = "product-detail"),

]