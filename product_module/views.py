from django.shortcuts import render
from .models import Product
# Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_module/product_list.html', {'products': products})
