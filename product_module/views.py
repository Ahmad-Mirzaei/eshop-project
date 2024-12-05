from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory
from django.http import Http404
from django.db.models import Avg, Min, Max
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views import View
from django.shortcuts import redirect

# Create your views here.

class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = "products"
    ordering = ["-price"]               # مرتب ‌سازی کالاها بر اساس قیمت
    paginate_by = 6                       # در هر صفحه چند کالا نمایش بدهد



    def get_queryset(self):
        base_query = super(ProductListView, self).get_queryset()
        data = base_query.filter(is_active = True)
        return data

# ----------------------------------------------------------------------------------------------------------------------

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_module/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_product = self.object
        request = self.request
        # favorite_product_id = request.session["product_favorite"]
        favorite_product_id = request.session.get("product_favorite")
        context["is_favorite"] = favorite_product_id == str(loaded_product.id)
        return context

# ----------------------------------------------------------------------------------------------------------------------

class AddProductFavorite(View):
    def post(self, request):
        product_id = request.POST["product_id"]
        product = Product.objects.get(pk=product_id)
        request.session["product_favorite"] = product_id
        return redirect(product.get_absolute_url())

# ----------------------------------------------------------------------------------------------------------------------



# ----------------------------------------------------------------------------------------------------------------------
