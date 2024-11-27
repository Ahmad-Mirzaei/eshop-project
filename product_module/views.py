from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory
from django.http import Http404
from django.db.models import Avg, Min, Max
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

# Create your views here.

class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = "products"

    def get_queryset(self):
        base_query = super(ProductListView, self).get_queryset()
        data = base_query.filter(is_active = True)
        return data

# ----------------------------------------------------------------------------------------------------------------------

class ProductDetailView(DetailView):
    template_name = 'product_module/product_detail.html'
    model = Product

# ----------------------------------------------------------------------------------------------------------------------

