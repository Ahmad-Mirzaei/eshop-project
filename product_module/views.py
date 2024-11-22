from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory
from django.http import Http404
from django.db.models import Avg
# Create your views here.
# ----------------------------------------------------------------------------------------------------------------------
def product_list(request):
    products = Product.objects.all().order_by("price")  # براساس کمترین قیمت مرتب کن
    context = {
        'products': products,
    }
    return render(request, 'product_module/product_list.html', context)

# ----------------------------------------------------------------------------------------------------------------------
def product_detail(request, slug):
    product = get_object_or_404(Product, slug = slug)
    return render(request, 'product_module/product_detail.html', {"product": product})

# ----------------------------------------------------------------------------------------------------------------------
