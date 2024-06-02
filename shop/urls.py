from django.urls import path
from shop.views import AddProductView, ProductListView

urlpatterns = [
    path('product/add/', AddProductView.as_view(), name='add_product'),
    path('product/list/', ProductListView.as_view(), name='product_list'),

]
