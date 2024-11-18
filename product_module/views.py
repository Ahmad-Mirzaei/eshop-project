from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import Http404
# Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_module/product_list.html', {'products': products})

def product_detail(request, pk):
    # step 1
    # try:
    #     product = Product.objects.get(id = pk)
    # except:
    #     raise Http404("گشتم نبود؛ نگرد نیست")

    # step 2
    product = get_object_or_404(Product, id = pk)
    return render(request, 'product_module/product_detail.html', {"product": product})