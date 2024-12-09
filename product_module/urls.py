from django.urls import path
from . import views

urlpatterns = [
    # path('', views.product_list, name='product-list'),
    path('', views.ProductListView.as_view(), name='product-list'),
    # path('<slug:slug>', views.product_detail, name='product-detail'),
    path('product-favorite', views.AddProductFavorite.as_view(), name='product-favorite'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product-detail'),
]
