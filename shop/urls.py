from django.urls import path
from rest_framework import routers
from shop.views import TestViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register(r'test', TestViewSet, basename='test')
router.register('products', ProductViewSet, basename='products')


urlpatterns = router.urls
