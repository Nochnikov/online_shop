from shop.models import Product, Category
from rest_framework import generics, mixins
from shop.serializers import AddProductSerializer, CategorySerializer, OrderSerializer


# Create your views here.

class AddProductView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = AddProductSerializer

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = AddProductSerializer

    '''Add filters to find via searching 
        And the newest and eldest items 
        via category
    '''

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MakeOrderView(generics.CreateAPIView):
    queryset = CategoryListView
    serializer_class = OrderSerializer



