from shop.models import Product, Category
from rest_framework import generics, mixins
from shop.serializers import AddProductSerializer, CategorySerializer, OrderSerializer, RetrieveProductSerializer
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


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = RetrieveProductSerializer

    """
        Seller can update his product as he wants. Include it. 
    """


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    """Only admins can update categories. Include it"""


class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategorySerializer

    """Only admins can create categories. Include it"""

class MakeOrCancelOrderView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    queryset = CategoryListView
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    """
        Person who wants to cancel order have to change only one field. Think what field!!
    """
