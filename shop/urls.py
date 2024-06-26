from django.urls import path
from shop.views import (
    AddProductView,
    ProductListView,
    ProductDetailDestroyUpdateView,
    OrderListRetrieveCancelView,
    MakeOrderView,
    CategoryListView,
    CategoryUpdateDeleteDetailView,
    CategoryCreateView)


urlpatterns = [
    # Seller
    path('product/add/', AddProductView.as_view(), name='add_product'),
    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailDestroyUpdateView.as_view(), name='product_detail'),

    # Customer
    path('product/makeorder/<int:product_id>/', MakeOrderView.as_view(), name='make_order'),

    path('myorders/list/', OrderListRetrieveCancelView.as_view(), name='order_list'),
    path('myorders/<int:pk>/', OrderListRetrieveCancelView.as_view(), name='order_detail'),
    path('myorders/<int:pk>/cancele/', OrderListRetrieveCancelView.as_view(), name='order_delete'),

    # admin only
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryUpdateDeleteDetailView.as_view(), name='category_detail'),

]

