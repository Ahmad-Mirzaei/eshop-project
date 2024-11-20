from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory
from django.http import Http404
from django.db.models import Avg
# Create your views here.

def product_list(request):
    products = Product.objects.all().order_by("price")  # براساس کمترین قیمت مرتب کن
    number_of_products = products.count()
    avg_rating = products.aggregate(Avg("rating"))
    context = {
        'products': products,
        'total_number_of_products': number_of_products,
        'avg_rating': avg_rating,
    }
    return render(request, 'product_module/product_list.html', context)


def product_detail(request, slug):
    # step 1
    # try:
    #     product = Product.objects.get(id = pk)
    # except:
    #     raise Http404("گشتم نبود؛ نگرد نیست")

    # step 2
    product = get_object_or_404(Product, slug = slug)
    return render(request, 'product_module/product_detail.html', {"product": product})


# for test git status --short