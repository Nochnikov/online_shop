from shop.models import Product, Category
from rest_framework import generics, mixins
from shop.serializers import AddProductSerializer, CategorySerializer, OrderSerializer
from shop.filters import ProductFilter
# Create your views here.

class AddProductView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = AddProductSerializer

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = AddProductSerializer
    filterset_class = ProductFilter

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategorySerializer

class MakeOrderView(generics.CreateAPIView):
    queryset = CategoryListView
    serializer_class = OrderSerializer




