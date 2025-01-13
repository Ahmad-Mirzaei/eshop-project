from django.db.models import Count
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import Product, ProductCategory, ProductBrand


class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 6

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super(ProductListView, self).get_context_data()
        query = Product.objects.all()
        product = query.order_by('-price').first()
        db_max_price = product.price if product is not None else 10000000
        context['db_max_price'] = db_max_price
        context['start_price'] = self.request.GET.get('start_price') or 0
        context['end_price'] = self.request.GET.get('start_price') or db_max_price
        return context

    def get_queryset(self):
        query = super(ProductListView, self).get_queryset()
        category_name = self.kwargs.get('cat')
        brand_name = self.kwargs.get('brand')
        request: HttpRequest = self.request
        start_price = request.GET.get('start_price')
        end_price = request.GET.get('end_price')

        if start_price is not None:
            query = query.filter(price__gte=start_price)

        if end_price is not None:
            query = query.filter(price__lte=end_price)

        if brand_name is not None:
            query = query.filter(brand__url_title__iexact=brand_name)

        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)
        return query


class ProductDetailView(DetailView):
    template_name = 'product_module/product_detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_product = self.object
        request = self.request
        favorite_product_id = request.session.get("product_favorites")
        context['is_favorite'] = favorite_product_id == str(loaded_product.id)
        return context


class AddProductFavorite(View):
    def post(self, request):
        product_id = request.POST["product_id"]
        product = Product.objects.get(pk=product_id)
        request.session["product_favorites"] = product_id
        return redirect(product.get_absolute_url())


def product_categories_component(request: HttpRequest):
    product_categories = ProductCategory.objects.filter(is_active=True, is_delete=False)
    context = {
        'categories': product_categories
    }
    return render(request, 'product_module/components/product_categories_component.html', context)


def product_brands_component(request: HttpRequest):
    product_brands = ProductBrand.objects.annotate(products_count=Count('product')).filter(is_active=True)
    context = {
        'brands': product_brands
    }
    return render(request, 'product_module/components/product_brands_component.html', context)
