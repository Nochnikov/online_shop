from django.contrib.auth import get_user_model
from rest_framework import serializers

from shop.models import Product, Category, Order


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'phone_number']

class AddProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image', 'category']

class RetrieveProductSerializer(serializers.ModelSerializer):

    seller_info = UserSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image', 'category', 'seller_info']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['user', 'status']