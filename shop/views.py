from django.http import Http404

from shop.models import Product, Category, Order
from rest_framework import generics, mixins
from shop.serializers import AddProductSerializer, CategorySerializer, OrderSerializer, RetrieveProductSerializer
from shop.filters import ProductFilter
from rest_framework import permissions

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


class ProductDetailDestroyUpdateView(generics.GenericAPIView,
                                     mixins.RetrieveModelMixin,
                                     mixins.UpdateModelMixin,
                                     mixins.DestroyModelMixin):
    queryset = Product.objects.all()
    serializer_class = RetrieveProductSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryUpdateDeleteDetailView(generics.GenericAPIView,
                                     mixins.RetrieveModelMixin,
                                     mixins.UpdateModelMixin,
                                     mixins.DestroyModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class CategoryCreateView(generics.CreateAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    permissions_classes = [permissions.DjangoModelPermissions]


class OrderListRetrieveCancelView(generics.GenericAPIView,
                                  mixins.UpdateModelMixin,
                                  mixins.ListModelMixin,
                                  mixins.RetrieveModelMixin):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk') is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class MakeOrderView(generics.CreateAPIView):
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        product_id = self.kwargs.get('product_id')

        try:
            product = Product.objects.all().get(pk=product_id)
        except Exception:
            raise f"Product with id {product_id} does not exist"

        order = serializer.save(user=self.request.user)

        order.order_item.add(product)
        order.total_price = product.price
        order.save()

