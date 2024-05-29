from shop.models import Product
from rest_framework import generics, mixins
from shop.serializers import AddProductSerializer


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

