from rest_framework import serializers

from shop.models import Product


class AddProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image', 'category']