from django.urls import path
from shop.views import AddProductView, ProductListView, ProductDetailDestroyUpdateView

urlpatterns = [
    path('product/add/', AddProductView.as_view(), name='add_product'),
    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailDestroyUpdateView.as_view(), name='product_detail'),
    path('product/<int:pk>/update/', ProductDetailDestroyUpdateView.as_view(), name='product_detail_update'),




]
