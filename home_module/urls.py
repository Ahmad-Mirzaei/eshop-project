from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='home_page'),
    path('contact_module-us', views.contact_page),
    # path('site-header', views.site_header_partial, name='site_header_partial')
]
