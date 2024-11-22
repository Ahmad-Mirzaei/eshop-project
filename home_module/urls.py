from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page),
    path('contact-us/', views.contact_page),
    # path('site-header/', views.site_header_partial, name = "site_header_partial"),

]